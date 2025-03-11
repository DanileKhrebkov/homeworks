class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, ISBN: {self.isbn}"


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []


    def borrow_book(self, book):
        self.borrowed_books.append(book)


    def return_book(self, book):
        self.borrowed_books.remove(book)


    def get_borrowed_books(self):
        return [book.title for book in self.borrowed_books]


class Library:
    def __init__(self):
        self.books = {}  
        self.readers = {}  
    def add_book(self, book):
        self.books[book.isbn] = book


    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]


    def register_reader(self, reader):
        self.readers[reader.reader_id] = reader


    def lend_book(self, isbn, reader_id):
        if isbn in self.books and reader_id in self.readers:
            book = self.books[isbn]
            reader = self.readers[reader_id]
            reader.borrow_book(book)
            del self.books[isbn]
        else:
            print("Книга или читатель не найдены.")


    def accept_returned_book(self, isbn, reader_id):
        if reader_id in self.readers:
            reader = self.readers[reader_id]
            for book in reader.borrowed_books:
                if book.isbn == isbn:
                    reader.return_book(book)
                    self.books[isbn] = book
                    break
        else:
            print("Читатель не найден.")



# Пользовательский код:
book1 = Book("1984", "George Orwell", 1949, "978-0451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0061120084")

reader1 = Reader("Иван Иванов", "001")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_reader(reader1)

library.lend_book("978-0451524935", "001")
print(f"Книги на руках у читателя: {reader1.get_borrowed_books()}")

library.accept_returned_book("978-0451524935", "001")
print(f"Книги на руках у читателя после возврата: {reader1.get_borrowed_books()}")