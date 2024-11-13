from abc import ABC, abstractmethod


class BookRepository(ABC):
    @abstractmethod
    def add_book(self, title, author_id, genre_id):
        pass

    @abstractmethod
    def edit_book(self, book_id, title, author_id, genre_id):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass

    @abstractmethod
    def load_books(self):
        pass


class AuthorRepository(ABC):
    @abstractmethod
    def add_author(self, name):
        pass

    @abstractmethod
    def edit_author(self, author_id, name):
        pass

    @abstractmethod
    def delete_author(self, author_id):
        pass

    @abstractmethod
    def load_authors(self):
        pass


class GenreRepository(ABC):
    @abstractmethod
    def add_genre(self, name):
        pass

    @abstractmethod
    def edit_genre(self, genre_id, name):
        pass

    @abstractmethod
    def delete_genre(self, genre_id):
        pass

    @abstractmethod
    def load_genres(self):
        pass
