"""
Command-line interface to interact with the Flask inventory API.
Allows adding, viewing, updating, deleting items, and fetching from external API.
"""
import requests

BASE = "http://127.0.0.1:5000/inventory"


def menu():
    """Print CLI menu options."""
    print("\nInventory CLI")
    print("1. View All Items")
    print("2. View Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Fetch Product by Name (OpenFoodFacts)")
    print("7. Exit")


def run_cli():
    """Main CLI loop."""
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            r = requests.get(BASE)
            print(r.json())
        elif choice == "2":
            id_ = input("Enter item ID: ")
            r = requests.get(f"{BASE}/{id_}")
            print(r.json())
        elif choice == "3":
            name = input("Name: ")
            brand = input("Brand: ")
            stock = int(input("Stock: "))
            price = float(input("Price: "))
            data = {"name": name, "brand": brand,
                    "stock": stock, "price": price}
            r = requests.post(BASE, json=data)
            print(r.json())
        elif choice == "4":
            id_ = input("Enter ID: ")
            price = float(input("New price: "))
            stock = int(input("New stock: "))
            r = requests.patch(
                f"{BASE}/{id_}", json={"price": price, "stock": stock})
            print(r.json())
        elif choice == "5":
            id_ = input("Enter ID to delete: ")
            r = requests.delete(f"{BASE}/{id_}")
            print(r.json())
        elif choice == "6":
            name = input("Enter product name: ")
            r = requests.get(f"{BASE}/fetch/{name}")
            print(r.json())
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    run_cli()
