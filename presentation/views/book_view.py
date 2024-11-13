from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QComboBox,
    QTreeWidget,
    QHeaderView,
)


class BookView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Book Tree Widget
        self.book_tree = QTreeWidget()
        self.book_tree.setColumnCount(3)
        self.book_tree.setHeaderLabels(["Book Title", "Author", "Genre"])
        header = self.book_tree.header()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.book_tree)

        # Form Layout
        form_layout = QHBoxLayout()
        self.title_input = QLineEdit()
        self.author_combo = QComboBox()
        self.genre_combo = QComboBox()
        form_layout.addWidget(QLabel("Title:"))
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(QLabel("Author:"))
        form_layout.addWidget(self.author_combo)
        form_layout.addWidget(QLabel("Genre:"))
        form_layout.addWidget(self.genre_combo)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Book")
        self.edit_button = QPushButton("Edit Book")
        self.delete_button = QPushButton("Delete Book")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
