from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import (
    employee_routes,
    skill_routes,
    employee_skill_routes,
    project_routes,
    project_members_routes
)
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(employee_routes.router)
app.include_router(skill_routes.router)
app.include_router(employee_skill_routes.router)
app.include_router(project_routes.router)
app.include_router(project_members_routes.router)
