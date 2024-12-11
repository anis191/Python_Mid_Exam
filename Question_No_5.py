class Library:
    book_list = []

    @classmethod
    def entry_book(cls, obj):
        cls.book_list.append(obj)

class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.authore = author
        self.availability = True
        Library.entry_book(self) 
    
    def borrow_book(self):
        if(self.availability is True):
            self.availability = False
            print(f"You successfully borrowed {self.title} book!")
        else:
            print(f"Sorry! {self.title} book is already borrowed")
    
    def return_book(self):
        if(self.availability is False):
            self.availability = True
            print("Thank's for return")
        else:
            print(f"This {self.title} book is not borrowed")

book1 = Book(112, "Python", "Anisul Alam")
book2 = Book(113, "Django", "Ariful Islam")

book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.borrow_book()
book1.borrow_book()