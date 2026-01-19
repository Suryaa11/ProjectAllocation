from app.db.connection import get_connection
from app.models.project_members import ProjectMembers  

class Project:

    @staticmethod
    def get_all_projects():
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM project"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        if result:
            projects = []
            for row in result:
                projects.append({
                    "Project_Id": row[0],
                    "Created_By": row[1],
                    "Project_Name": row[2],
                    "Start_Date": str(row[3]),
                    "End_Date": str(row[4])
                })
            return {"Projects": projects}
        return {"Error": "No projects found"}

    @staticmethod
    def get_project_by_id(project_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM project WHERE project_id = %s"
        cursor.execute(query, (project_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            project = {
                "Project_Id": result[0],
                "Created_By": result[1],
                "Project_Name": result[2],
                "Start_Date": str(result[3]),
                "End_Date": str(result[4])
            }
            return {"Project": project}
        return {"Error": "Project not found"}

    @staticmethod
    def create_project(project):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO project (created_by, project_name, start_date, end_date) VALUES (%s, %s, %s, %s)"
        values = (project.created_by, project.project_name, project.start_date, project.end_date)
        cursor.execute(query, values)
        conn.commit()

        project_id = cursor.lastrowid

        ProjectMembers.add_employee_to_project(project_id, project.created_by)

        cursor.close()
        conn.close()
        return {"Message": f"Project '{project.project_name}' created with ID {project_id} and creator added as member"}
