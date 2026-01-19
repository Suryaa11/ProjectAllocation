from fastapi import APIRouter,HTTPException
from app.models.employee_skill import EmployeeSkill
from app.schemas.employee_skill_schema import EmployeeSkillCreate

router = APIRouter(prefix="/employee_skills", tags=["EmployeeSkills"])

@router.get("/{emp_id}")
def view_skills_of_employee(emp_id:int):
    result=EmployeeSkill.view_skills_of_employee(emp_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.post("/{emp_id}")
def add_skill_to_employee(emp_skill:EmployeeSkillCreate):
    result=EmployeeSkill.add_skill_to_employee(emp_skill.emp_id,emp_skill.skill_id,emp_skill.skill_level)
    return result

@router.put("/")
def update_skill_level(updated_skill:EmployeeSkillCreate):
    result=EmployeeSkill.update_skill_level(updated_skill.emp_id,updated_skill.skill_id,updated_skill.skill_level)
    return result
