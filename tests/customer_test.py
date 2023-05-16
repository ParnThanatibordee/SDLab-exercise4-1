"""Tests of the Customer.

Author: Thanatibordee Sihaboonthong
"""

import re
import unittest 
from movierental.customer import Customer
from movierental.rental import Rental
from movierental.movie import Movie, PriceCode


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", 2000, ['demo'])
		self.regular_movie = Movie("CitizenFour", 2000, ['demo'])
		self.childrens_movie = Movie("Frozen", 2000, ['demo'])
		
	@unittest.skip("No convenient way to test")
	def test_billing(self):
		# no convenient way to test billing since its buried in the statement() method.
		pass

	def test_created_customer(self):
		self.assertEqual(self.c.get_name(), "Movie Mogul")
		self.assertFalse(self.c.rentals)

		customer = Customer("Johnny Depp")
		self.assertEqual(customer.get_name(), "Johnny Depp")
		self.assertFalse(customer.rentals)

	def test_add_rental(self):
		self.assertFalse(self.c.rentals)

		self.c.add_rental(Rental(self.new_movie, 1, PriceCode.new_release))

		self.assertTrue(self.c.rentals)
		self.assertEqual(len(self.c.rentals), 1)

	def test_add_repetitive_rental(self):
		self.assertFalse(self.c.rentals)

		movie = Rental(self.new_movie, 1, PriceCode.new_release)
		self.c.add_rental(movie)
		self.c.add_rental(movie)

		self.assertTrue(self.c.rentals)
		self.assertEqual(len(self.c.rentals), 1)

	def test_get_name(self):
		self.assertEqual(self.c.name, self.c.get_name())
	
	def test_statement(self):
		stmt = self.c.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, PriceCode.new_release))  # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_get_total_amount(self):
		self.c.add_rental(Rental(self.new_movie, 1, PriceCode.new_release))
		
		self.assertEqual(self.c.get_total_amount(), self.c.rentals[0].get_price())

		self.c.add_rental(Rental(self.regular_movie, 1, PriceCode.normal))
		self.c.add_rental(Rental(self.childrens_movie, 1, PriceCode.childrens))
		self.assertEqual(self.c.get_total_amount(), self.c.rentals[0].get_price() + self.c.rentals[1].get_price() + self.c.rentals[2].get_price())

	def test_get_frequent_amount(self):
		self.c.add_rental(Rental(self.new_movie, 1, PriceCode.new_release))
		
		self.assertEqual(self.c.get_frequent_renter_points(), self.c.rentals[0].get_frequent())

		self.c.add_rental(Rental(self.regular_movie, 1, PriceCode.normal))
		self.c.add_rental(Rental(self.childrens_movie, 1, PriceCode.childrens))
		self.assertEqual(self.c.get_frequent_renter_points(), self.c.rentals[0].get_frequent() + self.c.rentals[1].get_frequent() + self.c.rentals[2].get_frequent())

