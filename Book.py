
class Book:

    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title} by {self.author} in {self.category.name}"

