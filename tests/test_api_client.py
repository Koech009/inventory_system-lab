import pytest
from app.api_client import fetch_product_by_barcode


def test_fetch_product_by_barcode_valid(monkeypatch):
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

    def mock_get(url, headers=None, timeout=None):
        # Ensure headers are passed correctly
        assert "User-Agent" in headers
        assert "InventorySystem" in headers["User-Agent"]
        assert headers["Accept"] == "application/json"
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


def test_fetch_product_by_barcode_not_found(monkeypatch):
    import requests

    class MockResponse:
        status_code = 404

        def json(self):
            return {}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    product = fetch_product_by_barcode("0000000000000")
    assert "error" in product
    assert product["error"].startswith("API returned")
