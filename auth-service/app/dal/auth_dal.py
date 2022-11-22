from sqlmodel.ext.asyncio.session import AsyncSession

from app.model.auth import UserCreate, User


class AuthDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, data: UserCreate, ) -> User:
        new_user = data.dict()

        user = User(**new_user)
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return user
