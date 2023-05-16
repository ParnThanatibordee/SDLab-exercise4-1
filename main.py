# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movierental.movie import Movie, PriceCode
from movierental.rental import Rental
from movierental.customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", 2000, ['demo']),
        Movie("CitizenFour", 2000, ['demo']),
        Movie("Frozen", 2000, ['demo']),
        Movie("El Camino", 2000, ['demo']),
        Movie("Particle Fever", 2000, ['demo'])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.normal))
        days += 1
    print(customer.statement())
