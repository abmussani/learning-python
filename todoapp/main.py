from fastapi import FastAPI, Depends, Path, HTTPException
import models
from models import ToDo
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from requests import ToDoRequest

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/todos")
async def read_todos(db: db_dependency):
    return db.query(models.ToDo).all()

@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if todo is not None:
        return todo
    return HTTPException(status_code=404, detail="ToDo not found")

@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: ToDoRequest):
    todo = ToDo(**todo_request.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: ToDoRequest, todo_id: int = Path(gt=0)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.completed = todo_request.completed
    todo.priority = todo_request.priority
    
    db.add(todo)
    db.commit()
    return


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    db.query(models.ToDo).filter(models.ToDo.id == todo_id).delete()
    db.commit()
    return