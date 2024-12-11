class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.authore = author
        self.availability = True
    
    def borrow_book(self):
        if(self.availability is True):
            self.availability = False
            print(f"You successfully borrowed {self.title} book!")
        else:
            print(f"Sorry! {self.title} is already borrowed")

book1 = Book(112, "Python", "Anisul Alam")
book2 = Book(113, "Django", "Ariful Islam")
book1.borrow_book()
book1.borrow_book()
book2.borrow_book()
book2.borrow_book()