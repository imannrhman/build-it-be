from typing import List

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from app.core.database import get_async_session
from app.core.response import Response
from app.dal.product import ProductDAL
from app.depedencies.product import get_products_dal
from app.model.product import ProductRead, ProductCreate

product = APIRouter()



@product.get("",
             response_model=Response,
             status_code=http_status.HTTP_200_OK)
async def get_all_products(product_dal: ProductDAL = Depends(get_products_dal)):
    try:

        products = await product_dal.get_all_product()
        return Response(
            status_code=http_status.HTTP_200_OK,
            messages="Berhasil get data",
            results=products
        )
    except ValueError as e:
        return Response(
            status_code=http_status.HTTP_200_OK,
            messages=str(e),
            results=[]
        )
