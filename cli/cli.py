"""
Command-line interface to interact with the Flask inventory API.
"""

import requests
import json

BASE = "http://127.0.0.1:5000/inventory"


def menu():
    print("\nInventory CLI")
    print("1. View All Items")
    print("2. View Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Fetch Product by Barcode (OpenFoodFacts)")
    print("7. Exit")


def run_cli():
    while True:
        menu()
        choice = input("Choose an option: ")
        try:
            if choice == "1":
                r = requests.get(BASE)
                print(json.dumps(r.json(), indent=2))
            elif choice == "2":
                id_ = input("Enter item ID: ")
                r = requests.get(f"{BASE}/{id_}")
                print(json.dumps(r.json(), indent=2))
            elif choice == "3":
                name = input("Name: ")
                brand = input("Brand: ")
                stock = int(input("Stock: "))
                price = float(input("Price: "))
                barcode = input("Barcode (optional): ")
                data = {"name": name, "brand": brand,
                        "stock": stock, "price": price}
                if barcode:
                    data["barcode"] = barcode
                r = requests.post(BASE, json=data)
                print(json.dumps(r.json(), indent=2))
            elif choice == "4":
                id_ = input("Enter ID: ")
                price = float(input("New price: "))
                stock = int(input("New stock: "))
                r = requests.patch(
                    f"{BASE}/{id_}", json={"price": price, "stock": stock})
                print(json.dumps(r.json(), indent=2))
            elif choice == "5":
                id_ = input("Enter ID to delete: ")
                r = requests.delete(f"{BASE}/{id_}")
                print(json.dumps(r.json(), indent=2))
            elif choice == "6":
                barcode = input("Enter product barcode: ")
                r = requests.get(f"{BASE}/fetch/{barcode}")
                print(json.dumps(r.json(), indent=2))
            elif choice == "7":
                break
            else:
                print("Invalid choice")
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with API: {e}")


if __name__ == "__main__":
    run_cli()
