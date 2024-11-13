from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTreeWidget,
)


class GenreView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Genre Tree Widget
        self.genre_tree = QTreeWidget()
        self.genre_tree.setColumnCount(1)  # Only one column for genre name
        self.genre_tree.setHeaderLabels(["Genre Name"])  # Set header label
        layout.addWidget(self.genre_tree)

        # Form Layout
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        form_layout.addWidget(QLabel("Genre Name:"))
        form_layout.addWidget(self.name_input)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Genre")
        self.edit_button = QPushButton("Edit Genre")
        self.delete_button = QPushButton("Delete Genre")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
