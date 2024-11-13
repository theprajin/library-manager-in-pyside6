class Book:
    def __init__(self, id, title, author_id, genre_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Genre:
    def __init__(self, id, name):
        self.id = id
        self.name = name
