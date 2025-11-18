
class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def find_by_author(self, name):
        return [book for book in self.books if book.author.name.lower() == name.lower()]
