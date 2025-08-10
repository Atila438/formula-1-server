# services/driver_service.py
from data.drivers_data import drivers

def get_driver_by_name(name):
    return drivers.get(name.lower())

def get_all_drivers():
    return drivers

def add_driver(driver_id, driver_data):
    """Add a new driver to the dictionary."""
    if driver_id.lower() in drivers:
        return False
    drivers[driver_id.lower()] = driver_data
    return True

def update_fantasy_points(driver_id, points):
    """Update a driver's fantasy points."""
    driver = drivers.get(driver_id.lower())
    if driver:
        driver["fantasy_points"] += points
        return True
    return False