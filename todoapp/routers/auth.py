import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models import User
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from requests import UserRequest
from routers import auth
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import timedelta, timezone, datetime


router = APIRouter()

SECRET_KEY = 'cfcba3d5dbc0e6464606e31874218e3cb58854633c6fb7f16c1cfbca6935d8ea'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_bearer = OAuth2PasswordBearer(tokenUrl="auth/signin")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def get_current_user(token: str = Annotated[str, Depends(oauth_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        role: int = payload.get("role")
        if username is None or user_id is None:
            return HTTPException(status_code=400, detail="Could not validate user")
        return {"username": username, "id": user_id, "role": role}
    except JWTError:
        raise HTTPException(status_code=400, detail="Could not validate user")

user_dependency = Annotated[dict, Depends(get_current_user)]


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt_context.verify(password, user.hashed_password):
        return user
    return None

def create_access_token(username: str, user_id: int, role:str,  expires_delta:timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth/signin", status_code=status.HTTP_200_OK)
async def sign_in(db: db_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return HTTPException(status_code=400, detail="Invalid username or password")
    token = create_access_token(user.username, user.id, timedelta(minutes=30))
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/auth/me", status_code=status.HTTP_200_OK)
async def me(user: user_dependency, db: db_dependency):
    if user is None:
        return HTTPException(status_code=401, detail="Invalid authentication credentials")

    return user
