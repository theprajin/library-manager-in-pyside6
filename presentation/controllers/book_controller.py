# from PySide6.QtCore import QObject, Signal
# from PySide6.QtWidgets import QMessageBox, QTreeWidgetItem


# class BookController(QObject):
#     books_modified = Signal()

#     def __init__(self, view, book_model, author_model, genre_model):
#         super().__init__()
#         self.view = view
#         self.book_model = book_model
#         self.author_model = author_model
#         self.genre_model = genre_model

#         self.view.add_button.clicked.connect(self.add_book)
#         self.view.edit_button.clicked.connect(self.edit_book)
#         self.view.delete_button.clicked.connect(self.delete_book)
#         self.load_books()
#         self.load_authors()
#         self.load_genres()

#     def add_book(self):
#         title = self.view.title_input.text().strip()
#         author_name = self.view.author_combo.currentText()
#         genre_name = self.view.genre_combo.currentText()
#         author_id = next(
#             (
#                 id
#                 for id, name in self.author_model.load_authors()
#                 if name == author_name
#             ),
#             None,
#         )
#         genre_id = next(
#             (id for id, name in self.genre_model.load_genres() if name == genre_name),
#             None,
#         )

#         if title and author_id and genre_id:
#             self.book_model.add_book(title, author_id, genre_id)
#             self.load_books()
#             self.books_modified.emit()
#         else:
#             QMessageBox.warning(self.view, "Warning", "Please fill in all fields")

#     def edit_book(self):
#         selected_item = self.view.book_tree.currentItem()
#         if selected_item:
#             book_id = selected_item.data(0, 0)
#             title = self.view.title_input.text().strip()
#             author_name = self.view.author_combo.currentText()
#             genre_name = self.view.genre_combo.currentText()
#             author_id = next(
#                 (
#                     id
#                     for id, name in self.author_model.load_authors()
#                     if name == author_name
#                 ),
#                 None,
#             )
#             genre_id = next(
#                 (
#                     id
#                     for id, name in self.genre_model.load_genres()
#                     if name == genre_name
#                 ),
#                 None,
#             )

#             if title and author_id and genre_id:
#                 self.book_model.edit_book(book_id, title, author_id, genre_id)
#                 self.load_books()
#             else:
#                 QMessageBox.warning(self.view, "Warning", "Please fill in all fields")

#     def delete_book(self):
#         selected_item = self.view.book_tree.currentItem()
#         if selected_item:
#             book_id = selected_item.data(0, 0)
#             self.book_model.delete_book(book_id)
#             self.load_books()

#     def load_books(self):
#         self.view.book_tree.clear()
#         books = self.book_model.load_books()
#         for book_id, title, author_name, genre_name in books:
#             item = QTreeWidgetItem([title, author_name, genre_name])
#             item.setData(0, 0, book_id)
#             self.view.book_tree.addTopLevelItem(item)

#     def load_authors(self):
#         self.view.author_combo.clear()
#         authors = self.author_model.load_authors()
#         self.view.author_combo.addItems([name for _, name in authors])

#     def load_genres(self):
#         self.view.genre_combo.clear()
#         genres = self.genre_model.load_genres()
#         self.view.genre_combo.addItems([name for _, name in genres])


# presentation/controllers/book_controller.py

from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Signal, QObject


class BookController(QObject):
    books_modified = Signal()  # Signal to notify when books are modified

    def __init__(self, view, book_model, author_model, genre_model):
        super().__init__()
        self.view = view
        self.book_model = book_model
        self.author_model = author_model
        self.genre_model = genre_model

        # Connect buttons to their respective methods
        self.view.add_button.clicked.connect(self.add_book)
        self.view.edit_button.clicked.connect(self.edit_book)
        self.view.delete_button.clicked.connect(self.delete_book)

        # Load initial data
        self.load_books()
        self.load_authors()
        self.load_genres()

    def add_book(self):
        title = self.view.title_input.text().strip()
        author_name = self.view.author_combo.currentText()
        genre_name = self.view.genre_combo.currentText()

        # Find the author ID based on the selected author name
        author_id = next(
            (
                id
                for id, name in self.author_model.load_authors()
                if name == author_name
            ),
            None,
        )

        # Find the genre ID based on the selected genre name
        genre_id = next(
            (id for id, name in self.genre_model.load_genres() if name == genre_name),
            None,
        )

        if title and author_id and genre_id:
            if self.book_model.add_book(title, author_id, genre_id):
                self.load_books()
                self.books_modified.emit()  # Emit signal after adding a book
            else:
                QMessageBox.warning(self.view, "Error", "Failed to add book.")
        else:
            QMessageBox.warning(
                self.view, "Warning", "Book title, author, or genre cannot be empty."
            )

    def edit_book(self):
        selected_item = self.view.book_tree.currentItem()
        if selected_item:
            book_id = selected_item.data(0, Qt.UserRole)
            title = self.view.title_input.text().strip()
            author_name = self.view.author_combo.currentText()
            genre_name = self.view.genre_combo.currentText()

            # Find the author ID based on the selected author name
            author_id = next(
                (
                    id
                    for id, name in self.author_model.load_authors()
                    if name == author_name
                ),
                None,
            )

            # Find the genre ID based on the selected genre name
            genre_id = next(
                (
                    id
                    for id, name in self.genre_model.load_genres()
                    if name == genre_name
                ),
                None,
            )

            if title and author_id and genre_id:
                if self.book_model.edit_book(book_id, title, author_id, genre_id):
                    self.load_books()
                    self.books_modified.emit()  # Emit signal after editing a book
                else:
                    QMessageBox.warning(self.view, "Error", "Failed to update book.")
            else:
                QMessageBox.warning(
                    self.view,
                    "Warning",
                    "Book title, author, or genre cannot be empty.",
                )
        else:
            QMessageBox.warning(self.view, "Warning", "No book selected for editing.")

    def delete_book(self):
        selected_item = self.view.book_tree.currentItem()
        if selected_item:
            book_id = selected_item.data(0, Qt.UserRole)
            if self.book_model.delete_book(book_id):
                self.load_books()
                self.books_modified.emit()  # Emit signal after deleting a book
            else:
                QMessageBox.warning(self.view, "Error", "Failed to delete book.")
        else:
            QMessageBox.warning(self.view, "Warning", "No book selected for deletion.")

    def load_books(self):
        # Clear the current items in the book tree
        self.view.book_tree.clear()

        # Load books from the database
        books = self.book_model.load_books()

        # Populate the book tree with book title, author name, and genre name
        for book_id, title, author_name, genre_name in books:
            item = QTreeWidgetItem([title, author_name, genre_name])
            item.setData(0, Qt.UserRole, book_id)  # Store the book ID as hidden data
            self.view.book_tree.addTopLevelItem(item)

    def load_authors(self):
        # Clear the current items in the author combo box
        self.view.author_combo.clear()

        # Load authors from the database
        authors = self.author_model.load_authors()

        # Populate the author combo box with author names
        self.view.author_combo.addItems([name for _, name in authors])

    def load_genres(self):
        # Clear the current items in the genre combo box
        self.view.genre_combo.clear()

        # Load genres from the database
        genres = self.genre_model.load_genres()

        # Populate the genre combo box with genre names
        self.view.genre_combo.addItems([name for _, name in genres])
