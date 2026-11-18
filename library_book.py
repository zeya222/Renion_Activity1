# library_book.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

book1 = Book("The Little Prince", "Antoine de Saint‑Exupéry", 96)
book1.display_info()
