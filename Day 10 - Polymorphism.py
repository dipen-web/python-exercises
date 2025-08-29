# Create a Book class and overload __str__ to show book info.

# 1. Decide properties of book - title, author, year published

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # method
    def __str__(self):
        return f"Book title: {self.title}\nBook author: {self.author}\nYear published: {self.year}"

book1 = Book("Can't hurt me", "David Goggins", 2018)
print(book1)