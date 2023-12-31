'''
Write a library class with no_of_books and Books as two instance variables. Write a program to create a library frm this library class and show how you can prit all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books aftr the program sis stopped!!
'''

class Library:
    def __init__(self):
        self.noOfBooks = 0 
        self.books = [] 
    def addBooks(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)
    def showDetails(self):
        print(f"The number of books is {self.noOfBooks} and all books are: ")
        for i in range(len(self.books)):
            print(f"{i+1}. {self.books[i]}")

l1 = Library()
l1.showDetails()
l1.addBooks("Himu")
l1.addBooks("Michir Ali")
l1.addBooks("Amar bondho rashed")
l1.addBooks("Afganisthane ami Allah k dekhechi")
l1.addBooks("Kothao Keu Nei")
l1.addBooks("Nihir Valobasa")
l1.addBooks("Shovro")
l1.addBooks("3 A.M.")
l1.addBooks("3.10 A.M.")
l1.showDetails()