from pydantic import BaseModel

class ProjectMemberCreate(BaseModel):
    project_id: int
    emp_id: int
