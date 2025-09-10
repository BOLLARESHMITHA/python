"""
You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
1 Add a book to the library (Book ID, Title).
2 Remove a book using Book ID.
3 Search for a book by Book ID and display the title.
4 Update the title of a book (e.g., correction in title).
5 Display all books in the library.
6 Count the total number of books in the library.
7 Check if a book title exists in the library (reverse lookup).
"""

def add_book(books,new_book):
    id=list(new_book.keys())
    if(id[0] not in list(books.keys())):
        books.update(new_book)
    return books

def Remove_book(books,id):
    if(id in list(books.keys())):
        books.pop(id)
    return books

def Search_book(books,id):
    print("book with id = ",id," is ",books.get(id))

def Update_book_title(books,id):
    new_title=input("enter new title = ")
    new_t={id:new_title}
    books.update(new_t)
    return books

def Display_book(books):
    print("books in library = ",list(books.values()))

def Check_book(books,title):
    if(title in list(books.values())):
        print("book with title :",title," exists in the library")
    else:
        print("There is no book with title : ",title," in the library")


books=dict()
while(True):

    ch=int(input("Enter choice :"))

    if(ch>=1 and ch<=7):
        if(ch==1):
            b_id=input("Enter id of book :")
            b_title=input("enter title of book :")
            new_book={b_id:b_title}
            add_book(books,new_book)
        elif(ch==2):
            b_id=input("Enter id of book :")
            Remove_book(books,b_id)
        elif(ch==3):
            b_id=input("Enter id of book :")
            Search_book(books,b_id)
        elif(ch==4):
            b_id=input("Enter id of book :")
            Update_book_title(books,b_id)
        elif(ch==5):
            Display_book(books)
        elif(ch==6):
            print("Total number of books in the library = ",len(books))
        else:
            b_title=input("enter the title of book : ")
            Check_book(books,b_title)
    else:
        break