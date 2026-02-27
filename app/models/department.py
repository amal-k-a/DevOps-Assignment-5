from dataclasses import dataclass

@dataclass
class Department:
    id: str
    department_id: str
    department_name: str
    location: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return self.__dict__