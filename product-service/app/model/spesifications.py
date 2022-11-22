from uuid import UUID
from typing import Optional

from sqlmodel import SQLModel, Field

from app.core.model import UUIDModel, TimestampModel


class SpesificationKeyBase(SQLModel):
    key: Optional[str] = Field(max_length=255, nullable=True)


class SpesificationKey(UUIDModel, SpesificationKeyBase, TimestampModel, table=True):
    __tablename__ = "spesification_keys"


class SpesificationValueBase(SQLModel):
    value: Optional[str] = Field(max_length=255, nullable=True)


class GeneralSpesificationValue(UUIDModel, SpesificationValueBase, TimestampModel, table=True):
    __tablename__ = "spesification_values"


class SpesificationsBase(SQLModel):
    key: Optional[UUID] = Field(default=None, foreign_key="spesification_keys.id")
    value: Optional[UUID] = Field(default=None, foreign_key="spesification_values.id")


class Spesifications(UUIDModel, SpesificationsBase, TimestampModel, table=True):
    __tablename__ = "spesifications"
    product_id: Optional[str] = Field(default=None, foreign_key="products.id")
