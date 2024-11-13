import sys
from PySide6.QtWidgets import QApplication
from data.database import Database
from data.sqlite_repository import (
    SQLiteBookRepository,
    SQLiteAuthorRepository,
    SQLiteGenreRepository,
)
from presentation.controllers.book_controller import BookController
from presentation.controllers.author_controller import AuthorController
from presentation.controllers.genre_controller import GenreController
from presentation.views.book_view import BookView
from presentation.views.author_view import AuthorView
from presentation.views.genre_view import GenreView
from presentation.main_app import LibraryManagementApp

if __name__ == "__main__":
    app = QApplication(sys.argv)

    db = Database()
    book_repo = SQLiteBookRepository()
    author_repo = SQLiteAuthorRepository()
    genre_repo = SQLiteGenreRepository()

    book_view = BookView()
    author_view = AuthorView()
    genre_view = GenreView()

    book_controller = BookController(book_view, book_repo, author_repo, genre_repo)
    author_controller = AuthorController(author_view, author_repo)
    genre_controller = GenreController(genre_view, genre_repo)

    author_controller.authors_modified.connect(book_controller.load_authors)
    genre_controller.genres_modified.connect(book_controller.load_genres)

    main_window = LibraryManagementApp(
        book_controller,
        author_controller,
        genre_controller,
        book_view,
        author_view,
        genre_view,
    )
    main_window.show()

    sys.exit(app.exec())
