"""
Defines all API routes for the inventory management system.
Includes CRUD operations and external API fetch.
"""

from flask import Blueprint, jsonify, request
from .models import get_all_items, get_item, add_item, update_item, delete_item
from .api_client import fetch_product_by_barcode as fetch_product

# Create a Blueprint for inventory routes
inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/", methods=["GET"])
def all_inventory():
    """Retrieve all inventory items."""
    return jsonify(get_all_items()), 200


@inventory_bp.route("/<int:item_id>", methods=["GET"])
def single_inventory(item_id):
    """Retrieve a single inventory item by ID."""
    item = get_item(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@inventory_bp.route("/", methods=["POST"])
def create_inventory():
    """Add a new inventory item, optionally enriching with OpenFoodFacts data."""
    data = request.json or {}
    barcode = data.get("barcode")

    if barcode:
        product = fetch_product(barcode)
        if "error" not in product:
            data.update(product)

    new_item = add_item(data)
    return jsonify(new_item), 201


@inventory_bp.route("/<int:item_id>", methods=["PATCH"])
def update_inventory(item_id):
    """Update an existing inventory item by ID."""
    data = request.json or {}
    updated = update_item(item_id, data)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Item not found"}), 404


@inventory_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_inventory(item_id):
    """Delete an inventory item by ID."""
    deleted = delete_item(item_id)
    if deleted:
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404


@inventory_bp.route("/fetch/<string:barcode>", methods=["GET"])
def fetch_external(barcode):
    """Fetch product details from OpenFoodFacts API by barcode."""
    if not barcode.isdigit():
        return jsonify({"error": "Invalid barcode"}), 400

    product = fetch_product(barcode)

    # If product is a dict and has no "error" key, return it
    if isinstance(product, dict) and "error" not in product:
        return jsonify(product), 200

    return jsonify(product or {"error": "Product not found"}), 404
