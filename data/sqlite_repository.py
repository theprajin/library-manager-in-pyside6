from domain.repository import BookRepository, AuthorRepository, GenreRepository
from PySide6.QtSql import QSqlQuery


class SQLiteBookRepository(BookRepository):
    def add_book(self, title, author_id, genre_id):
        query = QSqlQuery()
        query.prepare("INSERT INTO Book (title, author_id, genre_id) VALUES (?, ?, ?)")
        query.addBindValue(title)
        query.addBindValue(author_id)
        query.addBindValue(genre_id)
        return query.exec()

    def edit_book(self, book_id, title, author_id, genre_id):
        query = QSqlQuery()
        query.prepare(
            "UPDATE Book SET title = ?, author_id = ?, genre_id = ? WHERE id = ?"
        )
        query.addBindValue(title)
        query.addBindValue(author_id)
        query.addBindValue(genre_id)
        query.addBindValue(book_id)
        return query.exec()

    def delete_book(self, book_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM Book WHERE id = ?")
        query.addBindValue(book_id)
        return query.exec()

    def load_books(self):
        query = QSqlQuery(
            "SELECT Book.id, Book.title, Author.name, Genre.name FROM Book LEFT JOIN Author ON Book.author_id = Author.id LEFT JOIN Genre ON Book.genre_id = Genre.id"
        )
        books = []
        while query.next():
            books.append(
                (query.value(0), query.value(1), query.value(2), query.value(3))
            )
        return books


class SQLiteAuthorRepository(AuthorRepository):
    def add_author(self, name):
        query = QSqlQuery()
        query.prepare("INSERT INTO Author (name) VALUES (?)")
        query.addBindValue(name)
        return query.exec()

    def edit_author(self, author_id, name):
        query = QSqlQuery()
        query.prepare("UPDATE Author SET name = ? WHERE id = ?")
        query.addBindValue(name)
        query.addBindValue(author_id)
        return query.exec()

    def delete_author(self, author_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM Author WHERE id = ?")
        query.addBindValue(author_id)
        return query.exec()

    def load_authors(self):
        query = QSqlQuery("SELECT id, name FROM Author")
        authors = []
        while query.next():
            authors.append((query.value(0), query.value(1)))
        return authors


class SQLiteGenreRepository(GenreRepository):
    def add_genre(self, name):
        query = QSqlQuery()
        query.prepare("INSERT INTO Genre (name) VALUES (?)")
        query.addBindValue(name)
        return query.exec()

    def edit_genre(self, genre_id, name):
        query = QSqlQuery()
        query.prepare("UPDATE Genre SET name = ? WHERE id = ?")
        query.addBindValue(name)
        query.addBindValue(genre_id)
        return query.exec()

    def delete_genre(self, genre_id):
        query = QSqlQuery()
        query.prepare("DELETE FROM Genre WHERE id = ?")
        query.addBindValue(genre_id)
        return query.exec()

    def load_genres(self):
        query = QSqlQuery("SELECT id, name FROM Genre")
        genres = []
        while query.next():
            genres.append((query.value(0), query.value(1)))
        return genres
