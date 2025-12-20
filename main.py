from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import v1
from api.v2 import v2

app = FastAPI(docs_url=None)

app.mount("/v1", v1)
app.mount("/v2", v2)
# app.include_router(auth.router)
# app.include_router(course.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
