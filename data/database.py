from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox
import sys


class Database:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("library_management.db")

        if not self.db.open():
            QMessageBox.critical(None, "Database Error", self.db.lastError().text())
            sys.exit(1)

        self.init_db()

    def init_db(self):
        query = QSqlQuery()
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS Author (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        """
        )
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS Genre (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        """
        )
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS Book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER,
                genre_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES Author(id),
                FOREIGN KEY (genre_id) REFERENCES Genre(id)
            )
        """
        )
