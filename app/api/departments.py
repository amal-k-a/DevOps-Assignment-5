from flask import Blueprint, jsonify
from app.services.department_service import DepartmentService

departments_bp = Blueprint("departments", __name__)
service = DepartmentService()

@departments_bp.route("/", methods=["GET"])
def get_departments():
    return jsonify(service.get_all()), 200