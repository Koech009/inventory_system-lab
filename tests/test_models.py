import pytest
import json
from app import models


def test_add_and_get_item(tmp_path):
    # Redirect inventory file to a temporary file
    test_file = tmp_path / "inventory.json"
    test_file.write_text("[]")
    models.DATA_FILE = str(test_file)

    # Add item
    item = {"name": "Milk", "brand": "DairyBest", "stock": 5, "price": 2.5}
    new_item = models.add_item(item)

    assert new_item["id"] == 1
    assert new_item["name"] == "Milk"

    # Get item
    fetched = models.get_item(1)
    assert fetched["brand"] == "DairyBest"


def test_update_and_delete_item(tmp_path):
    test_file = tmp_path / "inventory.json"
    test_file.write_text("[]")
    models.DATA_FILE = str(test_file)

    item = {"name": "Bread", "brand": "Bakery", "stock": 10, "price": 1.5}
    new_item = models.add_item(item)

    # Update
    updated = models.update_item(new_item["id"], {"stock": 20})
    assert updated["stock"] == 20

    # Delete
    deleted = models.delete_item(new_item["id"])
    assert deleted is True
    assert models.get_item(new_item["id"]) is None
