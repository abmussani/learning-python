from pydantic import BaseModel
from pydantic import Field
from typing import Optional, ClassVar, Dict, Any

class BookRequest(BaseModel):
    id : Optional[int] = Field(description="The ID is not needed on create", default=None)
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=500)
    rating: int = Field(ge=0, le=6)
    year: int = Field(ge=0, le=2026, default=2024)

    model_config: ClassVar[Dict[str, Any]] = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "john doe",
                "description": "This book is about ...",
                "rating": 5,
                "year": 2024
            }
        }
    }
