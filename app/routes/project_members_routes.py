from fastapi import APIRouter, HTTPException
from app.models.project_members import ProjectMembers
from app.schemas.project_members_schema import ProjectMemberCreate

router = APIRouter(prefix="/project_members", tags=["ProjectMembers"])

@router.post("/")
def add_employee_to_project(member: ProjectMemberCreate):
    result = ProjectMembers.add_employee_to_project(member.project_id, member.emp_id)
    return result

@router.delete("/")
def remove_employee_from_project(member: ProjectMemberCreate):
    result = ProjectMembers.remove_employee_from_project(member.project_id, member.emp_id)
    return result

@router.get("/project/{project_id}")
def view_employees_in_project(project_id: int):
    result = ProjectMembers.view_employees_in_project(project_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.get("/employee/{emp_id}")
def view_projects_of_employee(emp_id: int):
    result = ProjectMembers.view_projects_of_employee(emp_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result
