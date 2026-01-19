from pydantic import BaseModel
from enum import Enum


# For UserDefined Value to define Role of Employee
class Role(str,Enum):
    trainee = "trainee"
    senior_developer = "senior developer"
    TL = "TL"

# POST method
class EmployeeCreate(BaseModel):
    name:str
    mail_id:str
    role:Role

# PUT method
class EmployeeUpdate(BaseModel):
    role:Role

# GET Method
class EmployeeRead(BaseModel):
    emp_id: int
    name: str
    mail_id: str
    role: Role
