from dataclasses import dataclass

@dataclass
class Salary:
    id: str
    salary_id: str
    employee_id: str
    basic_salary: int
    bonus: int
    allowances: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return self.__dict__