
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def __repr__(self):
        return f"{self.name}, the author of {", ".join(str(book.title) for book in self.books)}"