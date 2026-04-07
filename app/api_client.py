"""
Handles integration with the OpenFoodFacts API.
Fetches product details using a barcode or product name.
"""

import requests
from .config import OPENFOODFACTS_API_URL


BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def fetch_product_by_barcode(barcode):
    if not barcode or not barcode.isdigit():
        return {"error": "Invalid barcode"}

    url = f"{BASE_URL}/{barcode}.json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return {"error": "Failed to reach external API"}

        data = response.json()
        product = data.get("product")
        if product:
            return {
                "barcode": barcode,
                "name": product.get("product_name") or "Unknown",
                "brand": product.get("brands") or "Unknown",
                "ingredients": product.get("ingredients_text") or "Not available",
            }
        return {"error": "Product not found in OpenFoodFacts"}
    except requests.exceptions.Timeout:
        return {"error": "External API timeout"}
    except requests.exceptions.RequestException:
        return {"error": "External API request failed"}
    except ValueError:
        return {"error": "Invalid response from external API"}
