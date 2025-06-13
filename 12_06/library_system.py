# Develop a simple library system using classes for `Book`, `Member`, and `Library`,
# with methods to add/remove books and members.

class Book:
    def __init__(self,bid,bname,quanity):
        self.bid = bid
        self.bname = bname
        self.quanity = quanity

class Member:
    def __init__(self,mid,mname):
        self.mid = mid
        self.mname = mname

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self,book):
        self.books[book.bid] = book

    def remove_book(self,bid):
        if bid in self.books.keys():
            self.books.pop(bid)
        else:
            print("book name is not valid")

    def add_member(self,member):
        self.members[member.mid] = member

    def remove_member(self,mid):
        if mid in self.members.keys():
            self.members.pop(mid)
        else:
            print("member name not valid")

    def display_book(self):
        if self.books:
            print("\nlibrary books")
            for book in self.books:
                print(book)
        else:
            print("no books in library")

    def display_member(self):
        if self.members:
            print("\nlibrary members: ")
            for member in self.members:
                print(member)
        else:
            print("no books in library")


library = Library()


book1 = Book(101,"aa",10)
book2 = Book(102,"bb",20)
library.add_book(book1)
library.add_book(book2)

member1 = Member(1,"aa")
member2 = Member(2,"bb")
library.add_member(member1)
library.add_member(member2)

library.display_book()
library.display_member()

library.remove_book(101)
library.remove_member(1)

library.display_book()
library.display_member()
