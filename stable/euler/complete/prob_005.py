# From: https://projecteuler.net/problem=5
from math import log

from sympy import primerange, floor, prod

if __name__ == "__main__":
    print(prod(prime ** floor(log(20, prime)) for prime in primerange(2, 21)))
