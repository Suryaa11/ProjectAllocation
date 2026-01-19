from app.db.connection import get_connection

class EmployeeSkill:

    @staticmethod
    def view_skills_of_employee(emp_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT e.emp_id, e.name, s.skill_name, es.skill_level
        FROM employee e
        JOIN employee_skill es ON e.emp_id = es.emp_id
        JOIN skill s ON s.skill_id = es.skill_id
        WHERE e.emp_id = %s
        """

        cursor.execute(query, (emp_id,))
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        if not result:
            return {"Error": "No Skill Found for this Employee"}

        skills = []
        for row in result:
            skills.append({
                "skill": row[2],
                "skill_level": row[3]
            })

        return {
            "emp_id": result[0][0],
            "name": result[0][1],
            "skills": skills
        }

    
    @staticmethod
    def add_skill_to_employee(emp_id,skill_id,skill_level):
        conn=get_connection()
        cursor=conn.cursor()
        query="INSERT INTO employee_skill (emp_id,skill_id,skill_level) VALUES (%s,%s,%s)"
        value=(emp_id,skill_id,skill_level.value)
        cursor.execute(query,value)
        conn.commit()
        cursor.close()
        conn.close()
        return {"Message":f"Skills Added to {emp_id}"}
    
    @staticmethod
    def update_skill_level(emp_id, skill_id, skill_level):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE employee_skill
        SET skill_level = %s
        WHERE emp_id = %s AND skill_id = %s
        """

        cursor.execute(query, (skill_level.value, emp_id, skill_id))
        conn.commit()

        cursor.close()
        conn.close()

        return {"Message": "Skill level updated successfully"}


        

