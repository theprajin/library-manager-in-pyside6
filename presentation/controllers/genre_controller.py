from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Signal, QObject


class GenreController(QObject):
    genres_modified = Signal()

    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

        self.view.add_button.clicked.connect(self.add_genre)
        self.view.edit_button.clicked.connect(self.edit_genre)
        self.view.delete_button.clicked.connect(self.delete_genre)

        self.load_genres()

    def add_genre(self):
        genre_name = self.view.name_input.text().strip()
        if genre_name:
            if self.model.add_genre(genre_name):
                self.load_genres()
                self.genres_modified.emit()
            else:
                QMessageBox.warning(self.view, "Error", "Failed to add genre.")
        else:
            QMessageBox.warning(self.view, "Warning", "Genre name cannot be empty.")

    def edit_genre(self):
        selected_genre = self.view.genre_tree.currentItem()
        if selected_genre:
            genre_id = selected_genre.data(0, Qt.UserRole)
            genre_name = self.view.name_input.text().strip()
            if genre_name:
                if self.model.edit_genre(genre_id, genre_name):
                    self.load_genres()
                    self.genres_modified.emit()
                else:
                    QMessageBox.warning(self.view, "Error", "Failed to update genre.")
            else:
                QMessageBox.warning(self.view, "Warning", "Genre name cannot be empty.")
        else:
            QMessageBox.warning(self.view, "Warning", "No genre selected for editing.")

    def delete_genre(self):
        selected_genre = self.view.genre_tree.currentItem()
        if selected_genre:
            genre_id = selected_genre.data(0, Qt.UserRole)
            if self.model.delete_genre(genre_id):
                self.load_genres()
                self.genres_modified.emit()
            else:
                QMessageBox.warning(self.view, "Error", "Failed to delete genre.")
        else:
            QMessageBox.warning(self.view, "Warning", "No genre selected for deletion.")

    def load_genres(self):
        self.view.genre_tree.clear()

        genres = self.model.load_genres()

        for genre_id, name in genres:
            item = QTreeWidgetItem([name])
            item.setData(0, Qt.UserRole, genre_id)
            self.view.genre_tree.addTopLevelItem(item)
