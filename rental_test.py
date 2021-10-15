import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.normal)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	def test_rental_price(self):
		# Movie.NEW_RELEASE
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		# Movie.REGULAR
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
		# Movie.CHILDRENS
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		# Movie.REGULAR
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_frequent(), 1.0)
		# Movie.CHILDRENS
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_frequent(), 1.0)
		# Movie.NEW_RELEASE
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_frequent(), 1.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_frequent(), 5.0)
		rental = Rental(self.new_movie, 2)
		self.assertEqual(rental.get_frequent(), 2.0)

