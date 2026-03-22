"""
Handles data operations for the inventory system.
CRUD operations are performed on a JSON file stored in data/inventory.json.
"""
import json
import os

DATA_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../data/inventory.json'))


def load_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_inventory(inventory):
    """
    Save the inventory list to the JSON file.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(inventory, f, indent=2)
    return inventory


def get_all_items():
    """
    Retrieve all inventory items.
    """
    return load_inventory()


def get_item(item_id=None):
    """
    Retrieve inventory items.
    """
    inventory = load_inventory()
    if item_id is None:
        return inventory
    return next((i for i in inventory if i['id'] == item_id), None)


def add_item(data):
    """
    Add a new item to the inventory.
    """
    inventory = load_inventory()
    new_id = max([i['id'] for i in inventory], default=0) + 1
    data['id'] = new_id
    inventory.append(data)
    save_inventory(inventory)
    return data


def update_item(item_id, data):
    """
    Update an existing item by ID.
    """
    inventory = load_inventory()
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        item.update(data)
        save_inventory(inventory)
        return item
    return None


def delete_item(item_id):
    """
    Delete an item from the inventory by ID.
    """
    inventory = load_inventory()
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        inventory.remove(item)
        save_inventory(inventory)
        return True
    return False
