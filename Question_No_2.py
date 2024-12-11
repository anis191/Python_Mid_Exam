class Book:
    def __init__(self,book_id,title,author,availability):
        self.book_id = book_id
        self.title = title
        self.authore = author
        self.availability = availability

book1 = Book(112, "Python", "Anisul Alam", True)

print(book1.book_id, book1.title, book1.authore, book1.availability)