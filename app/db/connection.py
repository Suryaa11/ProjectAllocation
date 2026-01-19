import mysql.connector

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootsql",
        database="project_allocation"
    )
    return conn

