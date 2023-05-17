"""Tests of the Movie.

Author: Thanatibordee Sihaboonthong
"""

import unittest
from movierental.customer import Customer
from movierental.rental import Rental
from movierental.movie import Movie, PriceCode


class PriceCodeTest(unittest.TestCase):
    """Tests of the PriceCode Enum class"""

    @classmethod
    def setUpClass(cls):
        """Set up an PriceCode Enum before test."""

        cls.new_release = PriceCode.new_release
        cls.normal = PriceCode.normal
        cls.childrens = PriceCode.childrens

        cls.new_movie = Movie("Mulan", 2023, ['demo'])
        cls.regular_movie = Movie("CitizenFour", 2000, ['demo'])
        cls.childrens_movie = Movie("Frozen", 2000, ['Children'])

    def test_price(self):
        self.assertEqual(self.new_release.price(1), 3)
        self.assertEqual(self.new_release.price(5), 15)

        self.assertEqual(self.normal.price(1), 2)
        self.assertEqual(self.normal.price(5), 6.5)

        self.assertEqual(self.childrens.price(1), 1.5)
        self.assertEqual(self.childrens.price(5), 4.5)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            self.new_release.price(0)
        
        with self.assertRaises(ValueError):
            self.new_release.price(-1)

        with self.assertRaises(ValueError):
            self.normal.price(0)
        
        with self.assertRaises(ValueError):
            self.normal.price(-1)

        
        with self.assertRaises(ValueError):
            self.childrens.price(0)
        
        with self.assertRaises(ValueError):
            self.childrens.price(-1)

    def test_frequent(self):
        self.assertEqual(self.new_release.frequent(1), 1)
        self.assertEqual(self.new_release.frequent(5), 5)

        self.assertEqual(self.normal.frequent(1), 1)
        self.assertEqual(self.normal.frequent(5), 1)

        self.assertEqual(self.childrens.frequent(1), 1)
        self.assertEqual(self.childrens.frequent(5), 1)

    def test_invalid_frequent(self):
        with self.assertRaises(ValueError):
            self.new_release.frequent(0)
        
        with self.assertRaises(ValueError):
            self.new_release.frequent(-1)

        with self.assertRaises(ValueError):
            self.normal.frequent(0)
        
        with self.assertRaises(ValueError):
            self.normal.frequent(-1)

        
        with self.assertRaises(ValueError):
            self.childrens.frequent(0)
        
        with self.assertRaises(ValueError):
            self.childrens.frequent(-1)

    def test_for_movie(self):
        self.assertIs(PriceCode.for_movie(self.new_movie), PriceCode.new_release)
        self.assertIs(PriceCode.for_movie(self.regular_movie), PriceCode.normal)
        self.assertIs(PriceCode.for_movie(self.childrens_movie), PriceCode.childrens)


class MovieTest(unittest.TestCase):
    """ Tests of the Movie class"""

    @classmethod
    def setUpClass(cls):
        """Set up an Movie class before test."""

        cls.new_movie = Movie("Mulan", 2000, ['demo'])
        cls.regular_movie = Movie("CitizenFour", 2000, ['demo'])
        cls.childrens_movie = Movie("Frozen", 2000, ['demo'])

    def test_get_title(self):
        self.assertEqual(self.new_movie.get_title(), "Mulan")
        self.assertEqual(self.regular_movie.get_title(), "CitizenFour")
        self.assertEqual(self.childrens_movie.get_title(), "Frozen")

    def test_get_year(self):
        self.assertEqual(self.new_movie.get_year(), 2000)
        self.assertEqual(self.regular_movie.get_year(), 2000)
        self.assertEqual(self.childrens_movie.get_year(), 2000)

    def test_get_genre(self):
        self.assertEqual(self.new_movie.get_genre(), ['demo'])
        self.assertEqual(self.regular_movie.get_genre(), ['demo'])
        self.assertEqual(self.childrens_movie.get_genre(), ['demo'])

    def test_str_magic_method(self):
        self.assertEqual(self.new_movie.get_title(), str(self.new_movie))
        self.assertEqual(self.regular_movie.get_title(), str(self.regular_movie))
        self.assertEqual(self.childrens_movie.get_title(), str(self.childrens_movie))

    def test_is_genre(self):
        self.assertTrue(self.new_movie.is_genre("demo"))
        self.assertTrue(self.regular_movie.is_genre("demo"))
        self.assertTrue(self.childrens_movie.is_genre("demo"))

    def test_invalid_is_genre(self):
        self.assertFalse(self.new_movie.is_genre(1))
        self.assertFalse(self.new_movie.is_genre(False))
