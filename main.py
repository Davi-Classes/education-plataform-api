import uuid
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Course(BaseModel):
    id: uuid.UUID
    title: str
    image_url: str
    description: Optional[str]

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


courses = [
    Course(
        id=uuid.uuid4(),
        title="Curso de ReactJS",
        image_url="https://wallpapercave.com/wp/wp2465923.jpg",
        description="Aprenda a biblioteca de frontend mais utilizada do mercado.",
    ),
    Course(
        id=uuid.uuid4(),
        title="APIs com FastAPI",
        image_url="https://dkrn4sk0rn31v.cloudfront.net/uploads/2022/03/o-que-e-fastapi.png",
        description="Desenvolvimento APIs assíncronas com FastAPI",
    ),
    Course(
        id=uuid.uuid4(),
        title="NextJS",
        image_url="https://dkrn4sk0rn31v.cloudfront.net/uploads/2021/01/conhecendo-o-next-js.png",
        description="Todo o poder de server side rendering e cache com NextJS",
    ),
    Course(
        id=uuid.uuid4(),
        title="Langchain",
        image_url="https://framerusercontent.com/images/wBIfkv9ElvdBDjilQHkMwNuNegI.webp?width=2400&height=1260",
        description="Aprenda o framework mais utilizado para criar agentes de inteligência artificial",
    ),
]

app = FastAPI(title="Education Plataform API")


@app.get("/courses")
def get_courses(search: Optional[str] = None) -> list[Course]:
    if search is not None:
        return [course for course in courses if search in course.title]

    return courses
