from sqlmodel import Field, SQLModel

from app.core.model import UUIDModel, TimestampModel


class UserBase(SQLModel):
    email: str = Field(max_length=255, nullable=True)
    password: str = Field(max_length=255)
    hash_password: str = Field(max_length=255)
    is_active: bool = Field()


class User(
    UUIDModel,
    UserBase,
    TimestampModel
):
    __tablename__ = 'users'


class UserCreate(UserBase):
    pass
