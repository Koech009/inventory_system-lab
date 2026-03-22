import pytest
from app.api_client import fetch_product_by_name


def test_fetch_product_by_name(monkeypatch):
    # Mock requests.get to avoid hitting real API
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self._json = json_data
            self.status_code = status_code

        def json(self):
            return self._json

    def mock_get(*args, **kwargs):
        return MockResponse({
            "products": [
                {"product_name": "Nutella", "brands": "Ferrero",
                    "ingredients_text": "Sugar, Palm Oil"}
            ]
        })

    monkeypatch.setattr("requests.get", mock_get)

    product = fetch_product_by_name("Nutella")
    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert "Sugar" in product["ingredients"]
