from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.core.model import UUIDModel, TimestampModel


class ImageBase(SQLModel):
    image_url: str = Field(max_length=255, nullable=True)
    product_id: Optional[str] = Field(max_length=255, foreign_key="products.id")
    product: Optional[str] = Relationship(back_populates="products")


class Image(UUIDModel, ImageBase, TimestampModel):
    __tablename__ = "images"
