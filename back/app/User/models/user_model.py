from pydantic import BaseModel, EmailStr
from .role_model import Role


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Role