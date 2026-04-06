from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"

# for creating user
class UserCreate(BaseModel):
    name: str
    role: str   # viewer / analyst / admin

# for response (what API returns)
class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    is_active: bool

    class Config:
        orm_mode = True