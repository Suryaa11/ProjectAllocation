from app.db.connection import get_connection

class Employee:

    @staticmethod
    def get_all_employees():
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT * FROM employee"
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        employees=[]
        if result:
            for i in range(len(result)):
                employees.append({
                "Emp_Id":result[i][0],
                "Name":result[i][1],
                "Mail_Id":result[i][2],
                "Role":result[i][3]
                })
            return {"Employees":employees}
        return {"Error":"No Employee exist"}
    
    @staticmethod
    def get_employee_by_id(emp_id):
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT * FROM employee WHERE emp_id = (%s)"
        value=(emp_id,)
        cursor.execute(query,value)
        result=cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            employee={
                "Emp_Id":result[0],
                "Name":result[1],
                "Mail_Id":result[2],
                "Role":result[3]
            }
            return {"Employee":employee}
        return {"Error":"Employee does not exist"}
    
    @staticmethod
    def create_employee(employee_create):
        conn=get_connection()
        cursor=conn.cursor()
        query="INSERT INTO employee (name,mail_id,role) VALUES (%s,%s,%s)"
        value=(employee_create.name,employee_create.mail_id,employee_create.role)
        cursor.execute(query,value)
        conn.commit()
        employee_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"Employee Created with Employee_Id": employee_id}
    
    @staticmethod
    def update_employee_role(emp_id,updated_role):
        conn=get_connection()
        cursor=conn.cursor()
        query="UPDATE employee SET role = (%s) WHERE emp_id = (%s)"
        value=(updated_role,emp_id)
        cursor.execute(query,value)
        conn.commit()
        cursor.close()
        conn.close()
        return {"Message": f"Employee {emp_id} role updated to {updated_role}"}


    @staticmethod
    def delete_employee(emp_id):
        conn=get_connection()
        cursor=conn.cursor()
        query="DELETE FROM employee WHERE emp_id = (%s)"
        value=(emp_id,)
        cursor.execute(query,value)
        conn.commit()
        cursor.close()
        conn.close()
        return {"Message": f"Employee {emp_id} deleted successfully"}
    
    @staticmethod
    def get_employee_full_details(emp_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT emp_id, name, mail_id, role FROM employee WHERE emp_id = %s", (emp_id,))
        emp = cursor.fetchone()
        if not emp:
            cursor.close()
            conn.close()
            return {"Error": "Employee does not exist"}

        employee = {
            "Emp_Id": emp[0],
            "Name": emp[1],
            "Mail_Id": emp[2],
            "Role": emp[3]
        }

        cursor.execute("""
            SELECT s.skill_name, es.skill_level
            FROM employee_skill es
            JOIN skill s ON es.skill_id = s.skill_id
            WHERE es.emp_id = %s
        """, (emp_id,))
        skills = cursor.fetchall()
        employee["Skills"] = [{"Skill": s[0], "Level": s[1]} for s in skills] if skills else []

        cursor.execute("""
            SELECT p.project_id, p.project_name
            FROM project_members pm
            JOIN project p ON pm.project_id = p.project_id
            WHERE pm.emp_id = %s
        """, (emp_id,))
        projects = cursor.fetchall()
        employee["Projects"] = [{"Project_Id": p[0], "Project_Name": p[1]} for p in projects] if projects else []

        cursor.close()
        conn.close()
        return {"Employee_Details": employee}



