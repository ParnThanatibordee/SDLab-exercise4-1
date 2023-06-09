"""Tests of the Rental.

Author: Thanatibordee Sihaboonthong
"""

import unittest
from movierental.customer import Customer
from movierental.rental import Rental
from movierental.movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", 2000, ['demo'])
		self.regular_movie = Movie("CitizenFour", 2000, ['demo'])
		self.childrens_movie = Movie("Frozen", 2000, ['demo'])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", 2000, ['demo'])
		r = Rental(m, 1, PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, r.get_price_code())

	def test_rental_price(self):
		# Movie.NEW_RELEASE
		rental = Rental(self.new_movie, 1, PriceCode.new_release)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_price(), 15.0)
		# Movie.REGULAR
		rental = Rental(self.regular_movie, 1, PriceCode.normal)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5, PriceCode.normal)
		self.assertEqual(rental.get_price(), 6.5)
		# Movie.CHILDRENS
		rental = Rental(self.childrens_movie, 1, PriceCode.childrens)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5, PriceCode.childrens)
		self.assertEqual(rental.get_price(), 4.5)

	def test_get_price_code(self):
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_price_code(), PriceCode.new_release)
	
	def test_get_movie(self):
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_movie(), self.new_movie)

	def test_get_days_rented(self):
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_days_rented(), 5)

	def test_get_price(self):
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_price_code(), PriceCode.new_release)

		self.assertEqual(rental.get_price_code().price(rental.days_rented), 15)

	def test_get_price_with_invalid_price_code(self):
		with self.assertLogs('rental', level='ERROR') as cm:
			rental = Rental(self.new_movie, 5, "invalid")
			rental.get_price()
			
			self.assertEqual(cm.output, [f'ERROR:rental:Movie {rental.get_movie()} has unrecognized priceCode {rental.get_price_code()}'])
		

	def test_rental_points(self):
		# Movie.REGULAR
		rental = Rental(self.regular_movie, 1, PriceCode.normal)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.regular_movie, 5, PriceCode.normal)
		self.assertEqual(rental.get_frequent(), 1.0)
		# Movie.CHILDRENS
		rental = Rental(self.childrens_movie, 1, PriceCode.childrens)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.childrens_movie, 5, PriceCode.childrens)
		self.assertEqual(rental.get_frequent(), 1.0)
		# Movie.NEW_RELEASE
		rental = Rental(self.new_movie, 1, PriceCode.new_release)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.get_frequent(), 5.0)
		rental = Rental(self.new_movie, 2, PriceCode.new_release)
		self.assertEqual(rental.get_frequent(), 2.0)

