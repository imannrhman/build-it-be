from typing import List

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from app.core.database import get_async_session
from app.dal.product import ProductDAL
from app.depedencies.product import get_products_dal
from app.model.product import ProductRead, ProductCreate

product = APIRouter()


@product.get("",
             response_model=List[ProductRead],
             status_code=http_status.HTTP_200_OK)
async def get_all_products():
    products = await get_products_dal()
    return products.get_all_product()

