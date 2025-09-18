from pydantic import BaseModel, Field

class ToDoRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100 )
    description: str = Field(min_length=1, max_length=300)
    completed: bool = False 
    priority: int = Field(gt=0, lt=6)

class UserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=100)
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=6)
    is_active: bool = True
    role: str = Field(min_length=1, max_length=20)

class ChangePasswordRequest(BaseModel):
    old_password: str = Field(min_length=6)
    new_password: str = Field(min_length=6)