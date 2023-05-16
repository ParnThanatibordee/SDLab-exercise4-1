from movierental.movie import PriceCode
import logging


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented, price_code: PriceCode):
		"""Initialize a new movie rental object for
		a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		# compute rental change
		if isinstance(self.price_code, PriceCode):
			return self.price_code.price(self.days_rented)
		else:
			log = logging.getLogger("rental")
			log.error(f"Movie {self.movie} has unrecognized priceCode {self.get_price_code()}")

	def get_frequent(self):
		# award renter points
		return self.price_code.frequent(self.days_rented)
