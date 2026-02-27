import os
from app.repositories.json_repository import JsonRepository
from app.models.salary import Salary

class SalaryService:
    def __init__(self):
        path = os.path.join(os.getcwd(), "data", "salaries.json")
        self.repo = JsonRepository(path, Salary)

    def get_all(self):
        return [s.to_dict() for s in self.repo.get_all()]