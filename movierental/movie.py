from enum import Enum
import datetime
import logging
import csv


class MovieCatalog:
    """Movie catalog from csv file."""

    def __init__(self):
        self.data = self.initial_movie()

    def initial_movie(self):
        temp = []
        data = []
        with open('movies.csv') as f:
            rows = csv.reader(f)
            for r in rows:
                temp.append(r)
        for i in temp[1:]:
            genre = i[3].split('|')
            data.append(Movie(i[1], int(i[2]), genre))
        return data

    def get_movie(self, title):
        for j in self.data:
            if j.get_title() == title:
                return j
        return None


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2.0 + (1.5 * (days - 2)) if (days > 2) else 2.0,
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + (1.5 * (days - 3)) if (days > 3) else 1.5,
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"
        if days > 0:
            pricing = self.value["price"]  # the enum member's price formula
            return pricing(days)
        else:
            raise ValueError('days should be a positive number')

    def frequent(self, days: int) -> float:
        "Return the frequent renter points for a given number of days"
        if days > 0:
            frequent = self.value["frp"]
            return frequent(days)
        else:
            raise ValueError('days should be a positive number')

    @classmethod
    def for_movie(cls, movie):
        current_date_time = datetime.datetime.now()
        date = current_date_time.date()
        if date.year == movie.get_year():
            price_code = cls.new_release
        elif movie.is_genre("Children"):
            price_code = cls.childrens
        else:
            price_code = cls.normal
        return price_code


class Movie:
    """A movie available for rent."""

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self._title = title
        self._year = year
        self._genre = genre

    def is_genre(self, string):
        if string in self._genre:
            return True
        return False

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_genre(self):
        return self._genre

    def __str__(self):
        return self._title

