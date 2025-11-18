from Author import Author
from Book import Book
from Bookstore import Bookstore
from Category import Category

def main():
    bookstore = Bookstore()
    category_sci_fi = Category("Sci-fi")
    category_romance = Category("Romance")

    # First we added the books like this, the author as a string and just passed the instance to the bookstore directly
    # We also add an author instance to the book instead of a string (like we did with the categories
    bookstore.add_book(Book("Dune", Author("Frank Herbert"), category_sci_fi))
    bookstore.add_book(Book("Pride and Prejudice", Author("Jane Austen"), category_romance))
    bookstore.add_book(Book("I Robot", Author("Isaac Asimov"), category_sci_fi))
    # If we have more than one book of one author we should really first create an author instance so that we actually refer to the same author instance:
    author_william_gibson = Author("William Gibson")
    bookstore.add_book(Book("Neuromancer", author_william_gibson, category_sci_fi))
    bookstore.add_book(Book("Mona Lisa Overdrive", author_william_gibson, category_sci_fi))

    # Now if we also want to add the book to the author, we need to split our code into several calls:
    author_sally_rooney = Author("Sally Rooney")
    # add sally to the book:
    book_normal_people = Book("Normal people", author_sally_rooney, category_romance)
    # add the book to sally's list of books:
    author_sally_rooney.add_book(book_normal_people)
    # and now add the book to the bookstore:
    bookstore.add_book(book_normal_people)
    # let's add another sally rooney book:
    book_conversations_with_friends = Book("Conversations with friends", author_sally_rooney, category_romance)
    # add the book to sally's list of books:
    author_sally_rooney.add_book(book_conversations_with_friends)
    # and add that too to the bookstore:
    bookstore.add_book(book_conversations_with_friends)

    # tests:
    print("Search for 'Dune':", bookstore.find_by_title("Dune"))

    print("Search for 'william gibson' as author:", bookstore.find_by_author("william gibson"))

    # see the __repr__ method print out Sally rooney and her books:
    print(author_sally_rooney)

if __name__ == '__main__':
    main()
