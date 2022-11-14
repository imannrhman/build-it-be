from fastapi import FastAPI

from app.routes.product import product

app = FastAPI()


app.include_router(product, prefix='/api/v1/products', tags=['product'])
