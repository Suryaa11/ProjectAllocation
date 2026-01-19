from fastapi import APIRouter,HTTPException
from app.models.skill import Skill
from app.schemas.skill_schema import SkillCreate

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.get("/")
def get_all_skills():
    result=Skill.get_all_skills()
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.post("/")
def add_new_skill(skill:SkillCreate):
    result=Skill.add_new_skill(skill.skill_name)
    return result
