from typing import List, Optional, Text

from pydantic import condecimal
from sqlmodel import SQLModel, Field, Relationship

from app.core.model import UUIDModel, TimestampModel
from app.model.category import Category
from app.model.image import Image
from app.model.spesifications import Spesifications


class ProductCategoryLink(SQLModel, Table=True):
    product_id: Optional[str] = Field(default=None, foreign_key="product.id", primary_key=True)
    category_id: Optional[str] = Field(default=None, foreign_key="category.id", primary_key=True)


class ProductBase(SQLModel):
    name: str = Field(max_length=255, nullable=False),
    sku: str = Field(max_length=8, nullable=False)
    slug: str = Field(max_length=255, nullable=True)
    description: Optional[Text] = Field(nullable=True)

    price: condecimal(max_digits=12, decimal_places=3) = Field(default=0),
    stock: int = Field(nullable=False, default=0)
    maximum_order: Optional[int] = Field(nullable=True)
    minimum_order: Optional[int] = Field(nullable=True)

    images: List["Image"] = Relationship(back_populates="images")
    categories: List["Category"] = Relationship(back_populates="categories", link_model=ProductCategoryLink)
    general_spesifications: List["Spesifications"] = \
        Relationship(back_populates="spesifications")
    size: List["Spesifications"] = \
        Relationship(back_populates="spesifications")
    technical: List["Spesifications"] = \
        Relationship(back_populates="spesifications")


class Product(
    UUIDModel,
    ProductBase,
    TimestampModel,
    Table=True
):
    __tablename__ = "products"


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    pass


class ProductPatch(ProductBase):
    pass
