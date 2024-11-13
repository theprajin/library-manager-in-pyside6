# from PySide6.QtGui import QAction
# from PySide6.QtWidgets import (
#     QMainWindow,
#     QStackedWidget,
#     QToolBar,
#     QWidget,
#     QVBoxLayout,
# )


# class LibraryManagementApp(QMainWindow):
#     def __init__(
#         self,
#         book_controller,
#         author_controller,
#         genre_controller,
#         book_view,
#         author_view,
#         genre_view,
#     ):

#         super().__init__()
#         self.setWindowTitle("Library Management System")
#         self.setGeometry(100, 100, 800, 600)

#         # Initialize controllers and views
#         self.book_controller = book_controller
#         self.author_controller = author_controller
#         self.genre_controller = genre_controller
#         self.book_view = book_view
#         self.author_view = author_view
#         self.genre_view = genre_view

#         # Stacked widget to switch between views
#         self.stacked_widget = QStackedWidget()
#         self.stacked_widget.addWidget(self.book_view)
#         self.stacked_widget.addWidget(self.author_view)
#         self.stacked_widget.addWidget(self.genre_view)

#         # Main layout
#         container = QWidget()
#         container_layout = QVBoxLayout()
#         container_layout.addWidget(self.stacked_widget)
#         container.setLayout(container_layout)
#         self.setCentralWidget(container)

#         # Setup toolbar for navigation
#         self.setup_toolbar()

#     def setup_toolbar(self):
#         toolbar = QToolBar("Navigation")
#         self.addToolBar(toolbar)

#         # Add "Manage Books" action
#         manage_books_action = QAction("Manage Books", self)
#         manage_books_action.triggered.connect(
#             lambda: self.stacked_widget.setCurrentWidget(self.book_view)
#         )
#         toolbar.addAction(manage_books_action)

#         # Add "Manage Authors" action
#         manage_authors_action = QAction("Manage Authors", self)
#         manage_authors_action.triggered.connect(
#             lambda: self.stacked_widget.setCurrentWidget(self.author_view)
#         )
#         toolbar.addAction(manage_authors_action)

#         # Add "Manage Genres" action
#         manage_genres_action = QAction("Manage Genres", self)
#         manage_genres_action.triggered.connect(
#             lambda: self.stacked_widget.setCurrentWidget(self.genre_view)
#         )
#         toolbar.addAction(manage_genres_action)


# presentation/main_app.py

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QToolBar,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
)


class LibraryManagementApp(QMainWindow):
    def __init__(
        self,
        book_controller,
        author_controller,
        genre_controller,
        book_view,
        author_view,
        genre_view,
    ):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 800, 600)

        self.book_controller = book_controller
        self.author_controller = author_controller
        self.genre_controller = genre_controller
        self.book_view = book_view
        self.author_view = author_view
        self.genre_view = genre_view

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.book_view)
        self.stacked_widget.addWidget(self.author_view)
        self.stacked_widget.addWidget(self.genre_view)

        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.addWidget(self.create_navigation_bar())
        container_layout.addWidget(self.stacked_widget)
        container.setLayout(container_layout)
        self.setCentralWidget(container)

    def create_navigation_bar(self):
        nav_bar = QWidget()
        nav_layout = QHBoxLayout()
        nav_bar.setLayout(nav_layout)

        self.manage_books_button = QPushButton("Manage Books")
        self.manage_books_button.clicked.connect(
            lambda: self.switch_view(self.book_view, self.manage_books_button)
        )

        self.manage_authors_button = QPushButton("Manage Authors")
        self.manage_authors_button.clicked.connect(
            lambda: self.switch_view(self.author_view, self.manage_authors_button)
        )

        self.manage_genres_button = QPushButton("Manage Genres")
        self.manage_genres_button.clicked.connect(
            lambda: self.switch_view(self.genre_view, self.manage_genres_button)
        )

        nav_layout.addWidget(self.manage_books_button)
        nav_layout.addWidget(self.manage_authors_button)
        nav_layout.addWidget(self.manage_genres_button)

        self.highlight_button(self.manage_books_button)

        self.apply_button_style()

        return nav_bar

    def switch_view(self, view, button):
        self.stacked_widget.setCurrentWidget(view)
        self.highlight_button(button)

    def highlight_button(self, button):
        self.manage_books_button.setProperty("selected", False)
        self.manage_authors_button.setProperty("selected", False)
        self.manage_genres_button.setProperty("selected", False)

        button.setProperty("selected", True)

        self.manage_books_button.style().unpolish(self.manage_books_button)
        self.manage_books_button.style().polish(self.manage_books_button)
        self.manage_authors_button.style().unpolish(self.manage_authors_button)
        self.manage_authors_button.style().polish(self.manage_authors_button)
        self.manage_genres_button.style().unpolish(self.manage_genres_button)
        self.manage_genres_button.style().polish(self.manage_genres_button)

    def apply_button_style(self):
        self.setStyleSheet(
            """
            QPushButton {
                padding: 8px 16px;
                border: 1px solid #3A3A3A;
                border-radius: 5px;
                background-color: #3A3A3A;
                color: white;
                font-weight: normal;
            }
            QPushButton[selected="true"] {
                font-weight: bold;
                background-color: #2A2A2A;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """
        )
