from fastapi import APIRouter,HTTPException
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate,EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/")
def get_all_employee():
    result=Employee.get_all_employees()
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.get("/{emp_id}")
def get_employee_by_id(emp_id:int):
    result=Employee.get_employee_by_id(emp_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result

@router.put("/{emp_id}")
def update_employee_role(emp_id:int,updated_role:EmployeeUpdate):
    result=Employee.update_employee_role(emp_id,updated_role.role)
    return result

@router.post("/")
def create_employee(employee_create:EmployeeCreate):
    result=Employee.create_employee(employee_create)
    return result

@router.delete("/{emp_id}")
def delete_employee(emp_id:int):
    result=Employee.delete_employee(emp_id)
    return result

@router.get("/full/{emp_id}")
def get_employee_full_details(emp_id: int):
    result = Employee.get_employee_full_details(emp_id)
    if "Error" in result:
        raise HTTPException(status_code=404, detail=result["Error"])
    return result
