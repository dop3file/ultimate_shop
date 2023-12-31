from datetime import timedelta, datetime
from typing import Type

import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import Session

from config import config
from database.utils import get_session
from database.models import User
from schemas import UserIn
from exceptions import UserNotFound, IncorrectPassword, UserExists
from tools.hash import Hash
from jose import jwt, JWTError


class UserCRUD:
    @staticmethod
    async def get_by_username(session: AsyncSession, username: str) -> User:
        user = await session.execute(
            select(User).filter(User.username == username)
        )
        return user.scalars().first()

    @staticmethod
    async def add(session: AsyncSession, user_in: UserIn) -> None:
        async with session.begin():
            new_user = User(
                username=user_in.username,
                password=user_in.password
            )
            session.add(new_user)


class UserService:
    def __init__(self, crud: Type[UserCRUD], session: AsyncSession):
        self.crud = crud
        self.session = session
        self.hash_service = Hash()

    async def authenticate_user(self, user_in: UserIn) -> bool:
        user = await self.crud.get_by_username(self.session, user_in.username)
        if not user:
            raise UserNotFound(detail=f"User with username {user_in.username} not found")
        if self.hash_service.verify_hash(user_in.password, user.password):
            return True
        raise IncorrectPassword(detail="Incorrect password")

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": datetime.now() + config.token_expire})
        encoded_jwt = jwt.encode(to_encode, config.auth_secret_key, algorithm=config.hash_algorithm)
        return encoded_jwt

    async def register(self, user_in: UserIn):
        user = UserIn(
            username=user_in.username,
            password=self.hash_service.hash(user_in.password)
        )
        try:
            await self.crud.add(self.session, user)
        except sqlalchemy.exc.IntegrityError:
            raise UserExists(f"User with username {user_in.username} exists")

