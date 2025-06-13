# Develop a simple library system using classes for `Book`, `Member`, and `Library`,
# with methods to add/remove books and members.

class book:
    def __init__(self,bid,bname,quanity):
        self.bid = bid
        self.bname = bname
        self.quanity = quanity

class member:
    def __init__(self,mid,mname):
        self.mid = mid
        self.mname = mname

class library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self,book):
        self.books[book.bid] = book

    def remove_book(self,bid):
        if bid in self.books:
            self.books.pop(bid)
        else:
            print("book name is not valid")

    def add_member(self,member):
        self.members[member.mid] = member

    def remove_member(self,mid):
        if mid in self.members:
            self.members.pop(mid)
        else:
            print("member name not valid")

    def display_book(self):
        if self.books:
            print("library books")
            for book in self.books.values():
                print(book)
        else:
            print("no books in library")

    def display_member(self):
        pass

