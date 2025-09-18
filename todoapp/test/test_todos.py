import pytest
from sqlalchemy import text
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from database import Base
from main import app
from routers.todo import get_db

from fastapi.testclient import TestClient
from fastapi import status
from routers.auth import get_current_user
from models import ToDo, User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test-todos.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass = StaticPool,
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_test_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

def current_user_dependency():
    return {"id": 1, "username": "testuser", "role": "admin"}

app.dependency_overrides[get_db] = get_test_db
app.dependency_overrides[get_current_user] = current_user_dependency

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    db = TestSessionLocal()
    # test_user = User(first_name="test",last_name="user",username="testuser", email="testuser@email.com", hashed_password="$2b$12$JeyS7itC2xGKksf6m0GeN.9uJfJukuNkOh0e59KfhyO/nH5wqMBwC", role="")
    # db.add(test_user)
    # db.commit()
    # db.refresh(test_user)
    
    todo = ToDo(title="Test ToDo", description="This is a test ToDo", owner_id=1, priority=1)

    
    db.add(todo)
    db.commit()
    yield todo
    # yield test_user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos"))
        # connection.execute(text("DELETE FROM users"))
        connection.commit()




def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        "id": 1,
        "title": "Test ToDo",
        "description": "This is a test ToDo",
        "completed": False,
        "priority": 1,
        "owner_id": 1
    }]

def test_read_todo_by_id():
    response = client.get("/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "title": "Test ToDo",
        "description": "This is a test ToDo",
        "completed": False,
        "priority": 1,
        "owner_id": 1
    }

def test_read_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_create_todo():
    todo_data = {
        "title": "New ToDo",
        "description": "This is a new ToDo",
        "completed": False,
        "priority": 2
    }
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == status.HTTP_201_CREATED

def test_update_todo():
    update_data = {
        "title": "Updated ToDo",
        "description": "This ToDo has been updated",
        "completed": True,
        "priority": 3
    }
    response = client.put("/todos/1", json=update_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT