from uuid import UUID

from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.core.model import UUIDModel, TimestampModel


class ImageBase(SQLModel):
    image_url: str = Field(max_length=255, nullable=True)


class Image(UUIDModel, ImageBase, TimestampModel, table=True):
    __tablename__ = "images"
    product_id: Optional[UUID] = Field(default=None, foreign_key="products.id")
    product: Optional[UUID] = Relationship(back_populates="images")
