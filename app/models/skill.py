from app.db.connection import get_connection

class Skill:

    @staticmethod
    def add_new_skill(skill_name):
        conn=get_connection()
        cursor=conn.cursor()
        query="INSERT INTO skill (skill_name) VALUES (%s)"
        value=(skill_name,)
        cursor.execute(query,value)
        conn.commit()
        skill_id=cursor.lastrowid
        cursor.close()
        conn.close()
        return {f"New Skill Added {skill_name} Id":skill_id}
    
    @staticmethod
    def get_all_skills():
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT * FROM skill ORDER BY skill_id"
        cursor.execute(query)
        result=cursor.fetchall()
        skills=[]
        if result:
            for i in range(len(result)):
                skills.append({
                "Skill Id":result[i][0],
                "Skill":result[i][1]
                })
            return {"Skills":skills}
        return {"Error":"No Skills Found"}