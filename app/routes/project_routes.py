from fastapi import APIRouter, HTTPException
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def get_all_projects():
    result=Project.get_all_projects()
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.get("/{project_id}")
def get_project_by_id(project_id:int):
    result=Project.get_project_by_id(project_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.post("/")
def create_project(project:ProjectCreate):
    result=Project.create_project(project)
    return result