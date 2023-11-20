from pydantic import BaseModel, EmailStr
from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"