from app.db.connection import get_connection

# List of default skills
DEFAULT_SKILLS = [
    "Python","Java","C++","JavaScript","TypeScript","SQL","MySQL",
    "PostgreSQL","MongoDB","REST API","FastAPI","Spring Boot","React",
    "HTML","CSS","Git","Docker","Kubernetes","AWS","Azure",
    "CI/CD","Unit Testing","Postman","API Testing","System Design",
    "Data Structures","Agile","Scrum"
]

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Employee table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            emp_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            mail_id VARCHAR(100) NOT NULL UNIQUE,
            role ENUM('trainee','senior developer','TL') NOT NULL
        ) AUTO_INCREMENT = 1001;
    """)

    # Skill table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skill (
            skill_id INT PRIMARY KEY AUTO_INCREMENT,
            skill_name VARCHAR(100) NOT NULL UNIQUE
        );
    """)

    # Employee Skill
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee_skill (
            emp_id INT,
            skill_id INT,
            skill_level ENUM('Beginner','Intermediate','Expert') NOT NULL,
            PRIMARY KEY(emp_id, skill_id),
            FOREIGN KEY(emp_id) REFERENCES employee(emp_id),
            FOREIGN KEY(skill_id) REFERENCES skill(skill_id)
        );
    """)

    # Project table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project (
            project_id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            project_name VARCHAR(100) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            FOREIGN KEY(created_by) REFERENCES employee(emp_id)
        ) AUTO_INCREMENT = 101;
    """)

    # Project members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS project_members (
            project_id INT,
            emp_id INT,
            PRIMARY KEY(project_id, emp_id),
            FOREIGN KEY(project_id) REFERENCES project(project_id) ON DELETE CASCADE,
            FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE
        );
    """)

    for skill in DEFAULT_SKILLS:
        cursor.execute("INSERT IGNORE INTO skill (skill_name) VALUES (%s)", (skill,))

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized with tables and default skills!")
