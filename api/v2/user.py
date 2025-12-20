import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel


class User(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


class SignUp(BaseModel):
    name: str
    email: EmailStr
    password: str


class SignIn(BaseModel):
    email: EmailStr
    password: str


security = HTTPBearer()
users = [User(id=uuid.uuid4(), name="Admin", email="admin@email.com", password="1234")]


router = APIRouter()


def get_current_user(bearer: HTTPAuthorizationCredentials = Depends(security)):
    _, user_id = bearer.credentials.split(":")
    user = next((user for user in users if str(user.id) == user_id), None)

    if user is None:
        raise HTTPException(
            detail="Your user does not exists.",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return user


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_current_user)):
    return user


@router.post("/sign-up", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def sign_up(body: SignUp):
    user = next((user for user in users if user.email == body.email), None)

    if user is not None:
        raise HTTPException(
            detail="Já existe um usuário cadsatrado com esse email.",
            status_code=status.HTTP_409_CONFLICT,
        )

    user = User(id=uuid.uuid4(), **body.model_dump())
    users.append(user)

    return user


@router.post("/sign-in")
def sign_in(body: SignIn):
    user = next((user for user in users if user.email == body.email), None)

    if user is None or user.password != body.password:
        raise HTTPException(
            detail="Credenciais inválidas.", status_code=status.HTTP_401_UNAUTHORIZED
        )

    return {"token": f"test_token:{user.id}"}
