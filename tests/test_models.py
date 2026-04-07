import pytest
from app import models


def test_get_all_items():
    items = models.get_all_items()
    assert isinstance(items, list)
    assert len(items) >= 5  # seeded mock DB has at least 5 items


def test_get_item_existing():
    item = models.get_item(1)
    assert item is not None
    assert item["name"] == "Organic Almond Milk"


def test_get_item_nonexistent():
    item = models.get_item(999)
    assert item is None


def test_add_item():
    new_item = {"name": "Test Juice",
                "brand": "TestBrand", "stock": 10, "price": 2.5}
    added = models.add_item(new_item)
    assert "id" in added
    assert added["name"] == "Test Juice"
    # Verify it was appended to inventory
    assert models.get_item(added["id"]) == added


def test_update_item_existing():
    # Add an item first
    item = {"name": "Test Bread",
            "brand": "TestBakery", "stock": 5, "price": 1.0}
    added = models.add_item(item)
    updated = models.update_item(added["id"], {"stock": 15})
    assert updated["stock"] == 15


def test_update_item_nonexistent():
    updated = models.update_item(999, {"stock": 50})
    assert updated is None


def test_delete_item_existing():
    # Add an item first
    item = {"name": "Test Yogurt",
            "brand": "TestBrand", "stock": 7, "price": 1.5}
    added = models.add_item(item)
    deleted = models.delete_item(added["id"])
    assert deleted is True
    assert models.get_item(added["id"]) is None


def test_delete_item_nonexistent():
    deleted = models.delete_item(999)
    assert deleted is False
