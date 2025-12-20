from fastapi import FastAPI
from . import course

v1 = FastAPI(title="Education Plataform API (Deprecated)")

v1.include_router(course.router)
