from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

from . import schemas, models, utils

from app.core.database import async_engine
from .routes.auth import auth

app = FastAPI(
    title="Auth Service",
    description="This is the auth.py service for Build It",
    version="0.1.0",
    openapi_url="/api/v1/auth/openapi.json",
    docs_url="/api/v1/auth/docs"
)


@app.on_event("startup")
async def startup():
    # create db tables
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


app.include_router(auth, prefix='/api/v1/auth', tags=['auth'])

#
# @app.post('/login')
# def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_async_session)):
#     user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
#
#     if not utils.verify_password(user_credentials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
#
#     access_token = auth.create_access_token(data={"user_id": user.id})
#
#     return {"token": access_token, "token_type": "Bearer", "expires_in": auth.ACCESS_TOKEN_EXPIRE_MINUTES + " seconds"}
#
#
# @app.post('/register', response_model=schemas.UserOut)
# def register(user: schemas.RegisterUser, db: Session = Depends(get_async_session())):
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.get('/refresh')
# def refresh(current_user: schemas.TokenData = Depends(auth.get_current_user)):
#     payload_exp = current_user.exp
#     if payload_exp.utcnow() < datetime.utcnow():
#         token = auth.create_refresh_token(data={"user_id": current_user.id})
#         return {"token": token, "token_type": "Bearer", "expires_in": auth.REFRESH_TOKEN_EXPIRE_MINUTES + " seconds"}
#     return {"message": "Token is still valid"}
