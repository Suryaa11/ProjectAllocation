from pydantic import BaseModel
from enum import Enum

class SkillLevel(str,Enum):
    beginner="Beginner"
    intermediate="Intermediate"
    expert="Expert"


class EmployeeSkillCreate(BaseModel):
    emp_id:int
    skill_id:int
    skill_level:SkillLevel
