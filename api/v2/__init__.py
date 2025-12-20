from fastapi import FastAPI
from . import course, user


v2 = FastAPI(title="Education Plataform API")

v2.include_router(user.router)
v2.include_router(course.router)
