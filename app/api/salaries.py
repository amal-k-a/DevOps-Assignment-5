from flask import Blueprint, jsonify
from app.services.salary_service import SalaryService

salaries_bp = Blueprint("salaries", __name__)
service = SalaryService()

@salaries_bp.route("/", methods=["GET"])
def get_salaries():
    return jsonify(service.get_all()), 200