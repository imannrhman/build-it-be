from typing import Optional

from sqlmodel import SQLModel, Field

from app.core.model import UUIDModel, TimestampModel


class SpesificationKeyBase(SQLModel):
    key: Optional[str] = Field(max_length=255, nullable=True)


class SpesificationKey(UUIDModel, SpesificationKeyBase, TimestampModel, Table=True):
    __tablename__ = "spesification_keys"


class SpesificationValueBase(SQLModel):
    value: Optional[str] = Field(max_length=255, nullable=True)


class GeneralSpesificationValue(UUIDModel, SpesificationValueBase, TimestampModel, Table=True):
    __tablename__ = "spesification_values"


class SpesificationsBase(SQLModel):
    key: Optional[str] = Field(default=None, foreign_key="general_products_key.id")
    value: Optional[str] = Field(default=None, foreign_key="general_products_value.id")
    product_id: Optional[str] = Field(default=None, foreign_key="product.id", primary_key=True)


class Spesifications(UUIDModel, SpesificationsBase, TimestampModel, Table=True):
    __tablename__ = "spesificcations"
