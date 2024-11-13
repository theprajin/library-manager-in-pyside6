from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Signal, QObject


class AuthorController(QObject):
    authors_modified = Signal()

    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model

        self.view.add_button.clicked.connect(self.add_author)
        self.view.edit_button.clicked.connect(self.edit_author)
        self.view.delete_button.clicked.connect(self.delete_author)

        self.load_authors()

    def add_author(self):
        author_name = self.view.name_input.text().strip()
        if author_name:
            if self.model.add_author(author_name):
                self.load_authors()
                self.authors_modified.emit()
            else:
                QMessageBox.warning(self.view, "Error", "Failed to add author.")
        else:
            QMessageBox.warning(self.view, "Warning", "Author name cannot be empty.")

    def edit_author(self):
        selected_author = self.view.author_tree.currentItem()
        if selected_author:
            author_id = selected_author.data(0, Qt.UserRole)
            author_name = self.view.name_input.text().strip()
            if author_name:
                if self.model.edit_author(author_id, author_name):
                    self.load_authors()
                    self.authors_modified.emit()
                else:
                    QMessageBox.warning(self.view, "Error", "Failed to update author.")
            else:
                QMessageBox.warning(
                    self.view, "Warning", "Author name cannot be empty."
                )
        else:
            QMessageBox.warning(self.view, "Warning", "No author selected for editing.")

    def delete_author(self):
        selected_author = self.view.author_tree.currentItem()
        if selected_author:
            author_id = selected_author.data(0, Qt.UserRole)
            if self.model.delete_author(author_id):
                self.load_authors()
                self.authors_modified.emit()
            else:
                QMessageBox.warning(self.view, "Error", "Failed to delete author.")
        else:
            QMessageBox.warning(
                self.view, "Warning", "No author selected for deletion."
            )

    def load_authors(self):
        self.view.author_tree.clear()

        authors = self.model.load_authors()

        for author_id, name in authors:
            item = QTreeWidgetItem([name])
            item.setData(0, Qt.UserRole, author_id)
            self.view.author_tree.addTopLevelItem(item)
