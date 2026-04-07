import pytest
from app.api_client import fetch_product_by_barcode


def test_fetch_product_by_barcode_valid(monkeypatch):
    # Mock requests.get to avoid hitting the real API
    import requests

    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "product": {
                    "product_name": "Nutella",
                    "brands": "Ferrero",
                    "ingredients_text": "Sugar, Palm Oil"
                }
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    product = fetch_product_by_barcode("1234567890123")
    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"
    assert product["ingredients"] == "Sugar, Palm Oil"


def test_fetch_product_by_barcode_invalid():
    product = fetch_product_by_barcode("abc")
    assert "error" in product
    assert product["error"] == "Invalid barcode"
