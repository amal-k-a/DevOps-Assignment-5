"""
Employee model.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, field


@dataclass
class Employee:
    id: str
    employee_id: str
    first_name: str
    last_name: str
    gender: str
    date_of_birth: str
    department_id: str
    is_active: bool = True

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})