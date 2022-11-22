from fastapi import FastAPI

from sqlmodel import SQLModel
from app.core.database import async_engine
from app.routes.product import product

app = FastAPI(openapi_url="/api/v1/product/openapi.json", doc_url="/api/v1/product/docs")


@app.on_event("startup")
async def startup():
    # create db tables
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


app.include_router(product, prefix='/api/v1/products', tags=['product'])
