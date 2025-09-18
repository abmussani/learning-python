from fastapi import FastAPI
import models
from database import engine
from routers import auth, todo, user, admin

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(admin.router, prefix="/admin/todos", tags=["admin/todos"])
app.include_router(todo.router, prefix="/todos", tags=["todos"])
app.include_router(user.router, prefix="/users", tags=["users"])
