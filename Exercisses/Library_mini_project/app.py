import datetime
import json


def add_time(func):
    def wrapper(*args, **kwargs):
        print(f"Registery time: {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper


class Book:
    total_books = 0
    Library = []

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = price

        Book.total_books += 1
        Book.Library.append(self)

    @property
    def price(self):
        return f"{self._price}$"

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print(f"Eroor: Price for {self.title} must be greater than zero")

    def __str__(self):
        return f"The name of the book is: {self.title}, Author is {self.author},Price is {self._price}$"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self._price
        }


@add_time
def save_library():
    file_path = "library.json"
    with open(file_path, "w") as file:
        json.dump([book.to_dict() for book in Book.Library], file, indent=4)
        print(f"Json file {file_path} was created")


book1 = Book("Harrypotter", "Rowlling", 24)
book2 = Book("Armin's Book", "Armin", 14)
book3 = Book("Coding", "Someone", 30)

save_library()
