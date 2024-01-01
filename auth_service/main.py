from datetime import timedelta
from typing import Union, Annotated

import sentry_sdk
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from config import config
import schemas
from database.utils import get_session
from services.user_service import UserService, UserCRUD


sentry_sdk.init(
    dsn=config.sentry_url,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
app = FastAPI()


@app.post("/token")
async def login_with_token(
    user_in: schemas.UserIn,
    session: AsyncSession = Depends(get_session)
):
    user_service = UserService(
        UserCRUD,
        session
    )

    await user_service.authenticate_user(user_in)
    access_token = user_service.create_access_token(
        data={"sub": user_in.username}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@app.post("/register")
async def register(
    user_in: schemas.UserIn,
    session: AsyncSession = Depends(get_session)
):
    user_service = UserService(
        UserCRUD,
        session
    )
    await user_service.register(user_in)
    return {"success": True}