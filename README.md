Project Resource Allocation System

Project Overview:
This project is an Project Resource Allocation System designed to manage employees, their skills, and project assignments. It provides a RESTful API built using FastAPI for CRUD operations on employees, skills, and projects, and allows efficient management of employee skill sets and project allocations. The project is intended for HR teams, project managers, or organizations needing a centralized employee-skill-project tracking system.

Features:
- Add, update, delete, and view employees.
- Manage skills and associate them with employees.
- Create and manage projects, including assigning employees to projects.
- Validate employee age and other constraints using Pydantic models.
- SQL database integration for persistent storage.
- API endpoints for CRUD operations on employees, skills, and projects.

Technologies Used:
- Backend: FastAPI, Python 
- Database: MySQL / SQLite
- Data Validation: Pydantic


Installation & Setup:
1. Clone the repository:
   git clone <repository-url>
   cd capstone-project

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Setup Database:
   - Create a MySQL database and tables as per the schema above.
   - Update database credentials in the project (usually in db.py).

5. Run the application:
   uvicorn main:app --reload
   - API runs at: http://127.0.0.1:8000

