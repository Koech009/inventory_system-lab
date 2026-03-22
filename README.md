# Inventory Management System

A modular Flask REST API and CLI tool for managing inventory items.  
Supports full CRUD operations on a local JSON file and integrates with the OpenFoodFacts API to fetch product details.

---

## 🚀 Features

- **CRUD Operations:** Add, view, update, and delete items stored in `inventory.json`.
- **External API Integration:** Fetch product details by name from OpenFoodFacts.
- **CLI Interface:** Simple command-line menu for interacting with the API.
- **Unit Tests:** Coverage for models, routes, API client, and CLI.

---

## 📂 Project Structure

inventory_system/
│
├── app/
│ ├── init.py # Flask app factory
│ ├── api_client.py # OpenFoodFacts integration
│ ├── models.py # CRUD logic for inventory.json
│ └── routes.py # API endpoints
│
├── cli/
│ └── cli.py # Command-line interface
│
├── data/
│ └── inventory.json # Local inventory storage
│
├── tests/ # Pytest test suite
│ ├── test_api_client.py
│ ├── test_models.py
│ └── test_routes.py
│
├── config.py # Configuration settings
└── README.md

---

## ⚙️ Installation

### Clone the repository:

```bash
git clone https://github.com/Koech009/inventory_system-lab
cd inventory_system
Install dependencies:
pip install -r requirements.txt
pipenv install


▶️ Usage
Run the Flask API:
flask run

API will be available at:
http://127.0.0.1:5000/inventory

Run the CLI:
python cli/cli.py

Menu options:

View All Items
View Item
Add Item
Update Item
Delete Item
Fetch Product by Name (OpenFoodFacts)
Exit
🧪 Running Tests
pytest -v
📌 Example API Endpoints
GET /inventory/ → List all items
GET /inventory/<id> → Get item by ID
POST /inventory/ → Add new item
PATCH /inventory/<id> → Update item
DELETE /inventory/<id> → Delete item
GET /inventory/fetch/<name> → Fetch product from OpenFoodFacts
```
