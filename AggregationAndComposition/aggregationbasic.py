# aggregation and composition are two types of association
# representing the relationship between two classes
# relationship between library and book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return [f"{book.title} = {book.author}" for book in self.books]
        
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library1 = Library("Library1")
book1 = Book("Book1", "Author1")
book2 = Book("Book2", "Author2")

library1.add_book(book1)
library1.add_book(book2)
print(library1.get_books())