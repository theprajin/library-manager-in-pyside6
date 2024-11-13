from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTreeWidget,
)


class AuthorView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Author Tree Widget
        self.author_tree = QTreeWidget()
        self.author_tree.setColumnCount(1)
        self.author_tree.setHeaderLabels(["Author Name"])
        layout.addWidget(self.author_tree)

        # Form Layout
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        form_layout.addWidget(QLabel("Author Name:"))
        form_layout.addWidget(self.name_input)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Author")
        self.edit_button = QPushButton("Edit Author")
        self.delete_button = QPushButton("Delete Author")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
