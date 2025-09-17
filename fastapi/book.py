

class Book:
    id : int 
    title: str
    author: str
    description: str
    rating: int
    year : int

    def __init__(self, id, title, author, description, rating, year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.year = year



