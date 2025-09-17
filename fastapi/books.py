from fastapi import FastAPI 
from fastapi import Body

BOOKS = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "category": "Fiction"},
    {"id": 2,"title": "Book 2", "author": "Author 2", "category": "Science"},
    {"id": 3,"title": "Book 3", "author": "Author 3", "category": "Science"},
    {"id": 4,"title": "Book 4", "author": "Author 4", "category": "History"},
    {"id": 5,"title": "Book 5", "author": "Author 5", "category": "Biography"},
]

app = FastAPI()

@app.get("/books")
def read_books():
    return BOOKS

# @app.get("/books/{id}")
# def read_book_by_id(id: int):
#     for book in BOOKS:
#         if book["id"] == id:
#             return book
#     return {"message": "Book not found"}

@app.get("/books/{title}")
def read_book_by_title(title:str, category: str = None):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold() and (category is None or book.get("category").casefold() == category.casefold()):
            return book
    return {"message": "Book not found"}

@app.post("/books")
def create_book(book: dict = Body()):
    # set id to max id + 1
    if BOOKS:
        book["id"] = max(book["id"] for book in BOOKS) + 1
    else:
        book["id"] = 1
    BOOKS.append(book)
    return book

@app.put("/books/{id}")
def update_book(id:int, updated_book: dict = Body()):
    # set id to max id + 1
    for i in range(len(BOOKS)):
        if BOOKS[i].get("id") == id:
            updated_book["id"] = id
            BOOKS[i] = updated_book
            return updated_book
    
    return {"message": "Book not found"}

@app.delete("/books/{id}")
def update_book(id:int):
    # set id to max id + 1
    for book in BOOKS:
        if book.get("id") == id:
            BOOKS.remove(book)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}

