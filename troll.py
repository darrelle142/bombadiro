class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    def __init__(self, books: list[Book] = None): #Tránh bẫy "mutable default argument"
        self.books = books if books else []

    def add_book(self, book: Book):
        self.books.append(book)

    @classmethod
    def from_list(cls, book_list: list[tuple[str,str]]) -> "Library": #Dùng "Library" khi class chưa khai báo xong
        return cls([Book(title,author) for title, author in book_list])
    
    def show_books(self):
        for book in self.books:
            print(book)
        return self.books

lib = Library()
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("Python 101", "Someone"))
lib.show_books()

lib2 = Library.from_list([("A", "B"), ("C", "D")])
lib2.show_books()
