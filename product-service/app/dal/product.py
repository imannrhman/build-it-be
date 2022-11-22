from typing import List
from uuid import UUID

from sqlmodel import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession

from app.model.product import ProductCreate, Product, ProductRead, ProductPatch


class ProductDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_product(self, data: ProductCreate) -> Product:
        values = data.dict()

        product = Product(**values)
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)

        return product

    async def get_all_product(self) -> List[Product]:
        try:
            statement = select(Product) \
                .order_by(Product.created_at)

            result = await self.session.execute(statement=statement)
            return result.scalars().all()
        except ValueError as e:
            return []

    async def get_product(self, product_id: str | UUID) -> Product:
        statement = select(Product) \
            .where(Product.id == product_id)

        results = await self.session.execute(statement=statement)
        product = results.scalar_one_or_none()

        return product

    async def update_product(self, product_id: str | UUID, data: ProductPatch) -> Product:
        product = await self.get_product(product_id=product_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(product, k, v)

        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)

        return product

    async def delete_product(self, product_id: str | UUID) -> bool:
        statements = delete(Product).where(Product.id == product_id)

        await self.session.execute(statements=statements)
        await self.session.commit()

        return True
