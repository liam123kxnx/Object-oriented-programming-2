class Library:
    def __init__(self, list, name ):
        self.name = name
        self.booklist = list 

    def displayBooks(self):
        print("we have the following books here library: ",self.name)
        for books in self.booklist:
           print(books)

    def addBook(self, books):
     self.booklist.append(books)
     print(books,"has been added successfully" )

library1=Library(["one-piece","bleach","black-clover"],"bankai")
library1.displayBooks()


library2=Library(["death-king","my hero academia", "jujitsu-kaisen"],"tensa")
library2.addBook("naruto")
library2.displayBooks()

library3=Library(["jazzed-up","bleach-tybw","getuga-tensho"],"zangetsu")
