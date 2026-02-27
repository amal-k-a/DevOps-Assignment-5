import os
from app.repositories.json_repository import JsonRepository
from app.models.department import Department

class DepartmentService:
    def __init__(self):
        # Locate the json file in your /data folder
        path = os.path.join(os.getcwd(), "data", "departments.json")
        self.repo = JsonRepository(path, Department)

    def get_all(self):
        return [d.to_dict() for d in self.repo.get_all()]