from abc import ABC, abstractmethod
from typing import Dict, List

class BookFlyweight:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"

class BookProxy:
    def __init__(self, book_flyweight: BookFlyweight, book_id: str):
        self._book_flyweight = book_flyweight
        self._book_id = book_id
        self._is_available = True

    def get_info(self, user: 'User') -> str:
        if user.has_access():
            return str(self._book_flyweight)
        return "Access denied"

    def borrow(self) -> bool:
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self) -> None:
        self._is_available = True

    @property
    def is_available(self) -> bool:
        return self._is_available

class User(ABC):
    @abstractmethod
    def has_access(self) -> bool:
        pass

class Reader(User):
    def has_access(self) -> bool:
        return True

class Librarian(User):
    def has_access(self) -> bool:
        return True

class LibraryFacade:
    def __init__(self):
        self._books: Dict[str, BookProxy] = {}
        self._flyweights: Dict[str, BookFlyweight] = {}

    def add_book(self, title: str, author: str, genre: str, book_id: str) -> None:
        if book_id not in self._flyweights:
            self._flyweights[book_id] = BookFlyweight(title, author, genre)
        self._books[book_id] = BookProxy(self._flyweights[book_id], book_id)

    def borrow_book(self, user: User, book_id: str) -> bool:
        if book_id in self._books and user.has_access():
            return self._books[book_id].borrow()
        return False

    def return_book(self, book_id: str) -> None:
        if book_id in self._books:
            self._books[book_id].return_book()

    def search_book(self, user: User, query: str) -> List[str]:
        results = []
        for book_id, proxy in self._books.items():
            info = proxy.get_info(user)
            if query.lower() in info.lower():
                results.append(f"{info} [{'Available' if proxy.is_available else 'Borrowed'}]")
        return results

if __name__ == "__main__":
    library = LibraryFacade()

    library.add_book("1984", "George Orwell", "Dystopian", "B001")
    library.add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", "B002")

    reader = Reader()
    librarian = Librarian()

    print("Reader borrows '1984':", library.borrow_book(reader, "B001"))
    print("Reader borrows 'The Hobbit':", library.borrow_book(reader, "B002"))
    print("Reader tries to borrow '1984' again:", library.borrow_book(reader, "B001"))

    library.return_book("B001")
    print("After returning '1984':", library.borrow_book(reader, "B001"))

    print("\nSearch results for 'Orwell':")
    for book in library.search_book(reader, "Orwell"):
        print(book)

    print("\nSearch results for 'Fantasy':")
    for book in library.search_book(librarian, "Fantasy"):
        print(book)