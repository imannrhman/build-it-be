from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool = True

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[int] = None
    exp: Optional[datetime] = None

