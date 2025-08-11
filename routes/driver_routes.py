# routes/driver_routes.py
from flask import Blueprint
import controllers.driver_controller as driver_controller

driver_bp = Blueprint("driver_bp", __name__)

driver_bp.route("/", methods=["GET"])(driver_controller.home)
driver_bp.route("/driver/<name>", methods=["GET"])(driver_controller.fetch_driver)
driver_bp.route("/drivers", methods=["GET"])(driver_controller.fetch_all_drivers)
driver_bp.route("/driver", methods=["POST"])(driver_controller.create_driver)
driver_bp.route("/driver/<name>/points", methods=["PATCH"])(driver_controller.add_points)