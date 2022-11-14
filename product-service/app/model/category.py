from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.core.model import UUIDModel, TimestampModel


class CategoryBase(SQLModel):
    name: str = Field(max_length=255, nullable=False)


class Category(
    UUIDModel,
    CategoryBase,
    TimestampModel,
    Table=True
):
    __tablename__ = "categories"


class CategoryRead(CategoryBase, UUIDModel):
    pass


class CategoryCreate(CategoryBase):
    pass


class CategoryPatch(CategoryBase):
    name: Optional[str] = Field(max_length=255)


class CategoryProduct(
    UUIDModel,
    CategoryBase,
    Table=True
):
    __tablename__ = "categories"
