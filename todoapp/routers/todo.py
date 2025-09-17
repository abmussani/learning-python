from fastapi import APIRouter, Depends, Path, HTTPException
from models import ToDo
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from requests import ToDoRequest
from routers import auth
from .auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todos")
async def read_todos(user: user_dependency, db: db_dependency):
    if user is None:
        return HTTPException(status_code=401, detail="Invalid authentication credentials")
    return db.query(ToDo).all()

@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        return HTTPException(status_code=401, detail="Invalid authentication credentials")
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if todo is not None:
        return todo
    return HTTPException(status_code=404, detail="ToDo not found")

@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, todo_request: ToDoRequest):
    if user is None:
        return HTTPException(status_code=401, detail="Invalid authentication credentials")
    todo = ToDo(**todo_request.model_dump(), owner_id=user['id'])
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, db: db_dependency, todo_request: ToDoRequest, todo_id: int = Path(gt=0)):
    if user is None:
        return HTTPException(status_code=401, detail="Invalid authentication credentials")
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    if todo.owner_id != user['id']:
        raise HTTPException(status_code=403, detail="Not authorized to update this ToDo")
    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.completed = todo_request.completed
    todo.priority = todo_request.priority
    
    db.add(todo)
    db.commit()
    return


@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    db.query(ToDo).filter(ToDo.id == todo_id).delete()
    db.commit()
    return