import pytest
from app import create_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Redirect inventory file to a temporary file
    test_file = tmp_path / "inventory.json"
    test_file.write_text("[]")

    # Patch models.DATA_FILE to use temp file
    from app import models
    models.DATA_FILE = str(test_file)

    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_get_all_items(client):
    response = client.get("/inventory/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_item(client):
    data = {"name": "Juice", "brand": "FreshCo", "stock": 3, "price": 4.0}
    response = client.post("/inventory/", json=data)
    assert response.status_code == 201
    assert response.get_json()["name"] == "Juice"


def test_update_item(client):
    data = {"name": "Bread", "brand": "Bakery", "stock": 10, "price": 1.5}
    response = client.post("/inventory/", json=data)
    item_id = response.get_json()["id"]

    update = {"stock": 20}
    response = client.patch(f"/inventory/{item_id}", json=update)
    assert response.status_code == 200
    assert response.get_json()["stock"] == 20


def test_delete_item(client):
    data = {"name": "Milk", "brand": "DairyBest", "stock": 5, "price": 2.5}
    response = client.post("/inventory/", json=data)
    item_id = response.get_json()["id"]

    response = client.delete(f"/inventory/{item_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item deleted"

    response = client.get(f"/inventory/{item_id}")
    assert response.status_code == 404


def test_fetch_external_product(client, monkeypatch):
    # Patch the alias used in routes
    from app import routes

    def mock_fetch(barcode):
        return {
            "barcode": barcode,
            "name": "Nutella",
            "brand": "Ferrero",
            "ingredients": "Sugar, Palm Oil"
        }

    monkeypatch.setattr(routes, "fetch_product", mock_fetch)

    response = client.get("/inventory/fetch/1234567890123")
    assert response.status_code == 200
    product = response.get_json()
    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
