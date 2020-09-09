# From: https://projecteuler.net/problem=26
from sympy import primerange

from recurring_decimal import repetend_length

if __name__ == "__main__":
    print(max(primerange(3, int(1e3)), key=repetend_length,))
