import pytest
from app import create_app


@pytest.fixture
def client():
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
