from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_async_session
from app.dal.product import ProductDAL


async def get_products_dal(sessions: AsyncSession = Depends(get_async_session)) -> ProductDAL:
    return ProductDAL(sessions)
