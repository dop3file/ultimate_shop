from datetime import timedelta
from typing import Union, Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

from config import config
import schemas
from database.utils import get_db


app = FastAPI()


def authenticate_user(username: str, password: str):
    ...


@app.post("/token", response_model=schemas.Token)
def login_with_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
):
    user = ...