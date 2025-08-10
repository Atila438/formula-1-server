# controllers/driver_controller.py
from flask import jsonify, request
from services.driver_service import (
    get_driver_by_name,
    get_all_drivers,
    add_driver,
    update_fantasy_points
)

def home():
    return "<h2>🏁 F1 Fantasy API</h2><p>Try /driver/hamilton or /drivers</p>"

def fetch_driver(name):
    driver = get_driver_by_name(name)
    if driver:
        return jsonify(driver), 200
    return jsonify({"error": "Driver not found"}), 404

def fetch_all_drivers():
    return jsonify(get_all_drivers()), 200

def create_driver():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Driver ID required"}), 400
    success = add_driver(data["id"], data)
    if success:
        return jsonify({"message": "Driver added successfully"}), 201
    return jsonify({"error": "Driver already exists"}), 409

def add_points(name):
    data = request.get_json()
    points = data.get("points", 0)
    success = update_fantasy_points(name, points)
    if success:
        return jsonify({"message": f"Added {points} points to {name}"}), 200
    return jsonify({"error": "Driver not found"}), 404