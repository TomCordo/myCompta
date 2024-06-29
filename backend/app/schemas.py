from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    password: str  # This is the plain password which will be hashed


class UserResponseModel(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str
