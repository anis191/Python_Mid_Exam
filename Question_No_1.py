class Library:
    book_list = []

    @classmethod
    def entry_book(cls, obj):
        cls.book_list.append(obj)

class Book:
    def __init__(self, name, writer):
        self.name = name
        self.writer = writer

book1 = Book("Physics", "Anisul Alam")
book2 = Book("Math", "Ariful Islam")

Library.entry_book(book1)
Library.entry_book(book2)

for books in Library.book_list:
    print(f"Book Name: {books.name}, Writer: {books.writer}")