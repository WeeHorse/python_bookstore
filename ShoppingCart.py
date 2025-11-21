class ShoppingCart:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return [book for book in self.books]