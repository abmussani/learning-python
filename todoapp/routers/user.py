from fastapi import APIRouter, Depends, Path, HTTPException
from models import User
# from database import engine, SessionLocal
from database_postgres import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from requests import UserRequest
from routers import auth
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/")
async def read_users(db: db_dependency):
    return db.query(User).all()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    user = User(
        username = user_request.username,
        email = user_request.email,
        first_name = user_request.first_name,
        last_name = user_request.last_name,
        hashed_password = bcrypt_context.hash(user_request.password),
        role = user_request.role,
        is_active = True
    )


    db.add(user)
    db.commit()

@router.put("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user_request: UserRequest, user_id: int = Path(gt=0)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.first_name = user_request.first_name
    user.last_name = user_request.last_name
    user.is_active = user_request.is_active
    user.phone_number = user_request.phone_number
    user.role = user_request.role
    
    db.add(user)
    db.commit()
    return
    