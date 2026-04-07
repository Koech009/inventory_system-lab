"""
Handles data operations for the inventory system.
CRUD operations are performed on a mock in-memory array.
"""

# Mock database
inventory = [
    {
        "id": 1,
        "name": "Organic Almond Milk",
        "brand": "Silk",
        "barcode": "737628064502",
        "stock": 25,
        "price": 3.99,
        "ingredients": "Filtered water, almonds, cane sugar, sea salt",
    },
    {
        "id": 2,
        "name": "Whole Wheat Bread",
        "brand": "Nature's Own",
        "barcode": "072250023429",
        "stock": 40,
        "price": 2.49,
        "ingredients": "Whole wheat flour, water, yeast, salt",
    },
    {
        "id": 3,
        "name": "Greek Yogurt",
        "brand": "Chobani",
        "barcode": "081954000015",
        "stock": 15,
        "price": 1.29,
        "ingredients": "Cultured pasteurized nonfat milk, live active cultures",
    },
    {
        "id": 4,
        "name": "Orange Juice",
        "brand": "Tropicana",
        "barcode": "048500001234",
        "stock": 30,
        "price": 4.49,
        "ingredients": "100% pure squeezed orange juice",
    },
    {
        "id": 5,
        "name": "Peanut Butter",
        "brand": "Jif",
        "barcode": "051500255555",
        "stock": 20,
        "price": 5.99,
        "ingredients": "Roasted peanuts, sugar, molasses, fully hydrogenated vegetable oils, salt",
    }
]


def get_all_items():
    """Retrieve all inventory items."""
    return inventory


def get_item(item_id=None):
    """Retrieve inventory items."""
    if item_id is None:
        return inventory
    return next((i for i in inventory if i['id'] == item_id), None)


def add_item(data):
    """Add a new item to the inventory."""
    new_id = max([i['id'] for i in inventory], default=0) + 1
    data['id'] = new_id
    inventory.append(data)
    return data


def update_item(item_id, data):
    """Update an existing item by ID."""
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        item.update(data)
        return item
    return None


def delete_item(item_id):
    """Delete an item from the inventory by ID."""
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        inventory.remove(item)
        return True
    return False
