from pydantic import BaseModel
from datetime import date

class ProjectCreate(BaseModel):
    project_name: str
    start_date: date
    end_date: date
    created_by: int


class ProjectResponse(BaseModel):
    project_id: int
    project_name: str
    start_date: date
    end_date: date
    created_by: int
