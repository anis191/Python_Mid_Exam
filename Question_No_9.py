class Library:
    book_list = []

    @classmethod
    def entry_book(cls, obj):
        cls.book_list.append(obj)

class Book:
    def __init__(self,book_id,title,author):
        self._book_id = book_id
        self._title = title
        self.__authore = author
        self._availability = True
        Library.entry_book(self) 
    
    def borrow_book(self):
        if(self._availability is True):
            self._availability = False
            print(f"You successfully borrowed {self._title} book!")
        else:
            print(f"Sorry! {self._title} book is already borrowed")
    
    def return_book(self):
        if(self._availability is False):
            self._availability = True
            print("Thank's for return")
        else:
            print(f"This {self._title} book is not borrowed")
    
    def view_book_info(self):
        print(f"Book id: {self._book_id}\nTitle: {self._title}")
        print(f"Author: {self.__authore}\nAvailability: {self._availability}")

book1 = Book(112, "Python", "Anisul Alam")
book2 = Book(113, "Django", "Ariful Islam")

while(True):
    print('''
1. View All Books
2. Borrow Book
3. Return Book
4. Exit.
''')
    n = int(input("Enter Option No: "))
    if(n == 1):
        for books in Library.book_list:
            books.view_book_info()
    elif(n == 2):
        bookID = int(input("Enter Book id: "))
        check = False
        for books in Library.book_list:
            if(books._book_id == bookID):
                check = True
                books.borrow_book()
                break
        if(check is False):
            print(f"There is no book with this code-{bookID}")
    elif(n == 3):
        bookID = int(input("Enter Book id: "))
        check = False
        for books in Library.book_list:
            if(books._book_id == bookID):
                books.return_book()
                check = True
                break
        if(check is False):
            print(f"You can't borrowed any book with this code-{bookID}")
    else:
        break