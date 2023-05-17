"""Tests of the Movie.

Author: Thanatibordee Sihaboonthong
"""

import unittest
from movierental.customer import Customer
from movierental.rental import Rental
from movierental.movie import Movie, PriceCode


class MovieTest(unittest.TestCase):
    """ Tests of the Movie class"""
    
    def setUp(self):
        """Set up an Movie class before test."""
        
        self.new_movie = Movie("Mulan", 2000, ['demo'])
        self.regular_movie = Movie("CitizenFour", 2000, ['demo'])
        self.childrens_movie = Movie("Frozen", 2000, ['demo'])

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
