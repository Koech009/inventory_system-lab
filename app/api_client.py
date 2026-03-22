"""
Handles integration with the OpenFoodFacts API.
Fetches product details by product name.
"""
import requests


def fetch_product_by_name(name):
    """
    Search for product details from OpenFoodFacts using a product name.
    """
    url = (
        f"https://world.openfoodfacts.org/cgi/search.pl?"
        f"search_terms={name}&search_simple=1&action=process&json=1"
    )
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("products"):
                product = data["products"][0]
                return {
                    "name": product.get("product_name"),
                    "brand": product.get("brands"),
                    "ingredients": product.get("ingredients_text"),
                }
    except Exception as e:
        print(f"API error: {e}")
    return None
