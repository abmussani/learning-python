from fastapi import FastAPI, Path, Query, HttpException
from book import Book
from requests import BookRequest 


app = FastAPI()


BOOKS = [
    Book(1, "Title One", "Author One", "Description One", 5, 2023),
    Book(2, "Title Two", "Author Two", "Description Two", 4, 2022),
    Book(3, "Title Three", "Author Three", "Description Three", 5,1800),
    Book(4, "Title Four", "Author Four", "Description Four", 3, 2021),
    Book(5, "Title Five", "Author Five", "Description Five", 1, 1850),
    Book(6, "Title Six", "Author Six", "Description Six", 2, 1943),
]

@app.get("/books")
def read_books():
    return BOOKS

@app.get("/books/search/ratings/{book_rating}")
def read_book_by_rating(book_rating: int = Path(ge=0, le=6)):
    books = [book for book in BOOKS if book.rating >= book_rating]
    return books

@app.get("/books/search/year/{published_year}")
def read_book_by_year(published_year: int):
    books = [book for book in BOOKS if book.year == published_year]
    return books

@app.post("/books")
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book.id = find_book_id()
    BOOKS.append(new_book)
    return new_book



@app.put("/books/{book_id}")
def update_book(book_id: int, book_request: BookRequest):
    book = next((book for book in BOOKS if book.id == book_id), None)
    if book is None:
        return HttpException(status_code=404, detail="Book not found")
    book.title = book_request.title
    book.author = book_request.author
    book.description = book_request.description
    book.rating = book_request.rating
    book.year = book_request.year
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = next((book for book in BOOKS if book.id == book_id), None)
    if book is None:
        return HttpException(status_code=404, detail="Book not found")
    BOOKS.remove(book)
    return {"message": "Book deleted successfully"}





def find_book_id():
    return 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    