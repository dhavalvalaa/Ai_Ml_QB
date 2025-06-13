# Book Class
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id})"

# Member Class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

# Library Class
class Library:
    def __init__(self):
        self.books = {}  # Stores books using book_id as key
        self.members = {}  # Stores members using member_id as key

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Book '{removed_book.title}' removed from library.")
        else:
            print("Book not found!")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' registered.")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed_member = self.members.pop(member_id)
            print(f"Member '{removed_member.name}' removed.")
        else:
            print("Member not found!")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                print(book)
        else:
            print("No books in the library.")

    def display_members(self):
        if self.members:
            print("Library Members:")
            for member in self.members.values():
                print(member)
        else:
            print("No members registered.")

# Example Usage
library = Library()

# Adding books
book1 = Book("Python Programming", "John Doe", 101)
book2 = Book("Data Structures", "Jane Smith", 102)
library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member("Alice", 1)
member2 = Member("Bob", 2)
library.add_member(member1)
library.add_member(member2)

# Displaying books and members
library.display_books()
library.display_members()

# Removing a book and a member
library.remove_book(101)
library.remove_member(1)

# Display after removal
library.display_books()
library.display_members()
