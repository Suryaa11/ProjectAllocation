from app.db.connection import get_connection

class ProjectMembers:

    @staticmethod
    def add_employee_to_project(project_id, emp_id):
        conn = get_connection()
        cursor = conn.cursor()

        # Optional: check if employee already assigned
        check_query = "SELECT * FROM project_members WHERE project_id=%s AND emp_id=%s"
        cursor.execute(check_query, (project_id, emp_id))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return {"Message": f"Employee {emp_id} is already assigned to project {project_id}"}

        query = "INSERT INTO project_members (project_id, emp_id) VALUES (%s, %s)"
        cursor.execute(query, (project_id, emp_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"Message": f"Employee {emp_id} added to project {project_id}"}

    @staticmethod
    def remove_employee_from_project(project_id, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM project_members WHERE project_id=%s AND emp_id=%s"
        cursor.execute(query, (project_id, emp_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"Message": f"Employee {emp_id} removed from project {project_id}"}

    @staticmethod
    def view_employees_in_project(project_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT e.emp_id, e.name, e.mail_id, e.role
            FROM employee e
            JOIN project_members pm ON e.emp_id = pm.emp_id
            WHERE pm.project_id = %s
        """
        cursor.execute(query, (project_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        if result:
            employees = []
            for row in result:
                employees.append({
                    "Emp_Id": row[0],
                    "Name": row[1],
                    "Mail_Id": row[2],
                    "Role": row[3]
                })
            return {"Employees": employees}
        return {"Error": "No employees found in this project"}

    @staticmethod
    def view_projects_of_employee(emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT p.project_id, p.project_name, p.start_date, p.end_date
            FROM project p
            JOIN project_members pm ON p.project_id = pm.project_id
            WHERE pm.emp_id = %s
        """
        cursor.execute(query, (emp_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        if result:
            projects = []
            for row in result:
                projects.append({
                    "Project_Id": row[0],
                    "Project_Name": row[1],
                    "Start_Date": str(row[2]),
                    "End_Date": str(row[3])
                })
            return {"Projects": projects}
        return {"Error": "No projects found for this employee"}
