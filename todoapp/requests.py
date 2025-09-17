from pydantic import BaseModel, Field

class ToDoRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100 )
    description: str = Field(min_length=1, max_length=300)
    completed: bool = False 
    priority: int = Field(gt=0, lt=6)

