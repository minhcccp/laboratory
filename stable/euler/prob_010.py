# From: https://projecteuler.net/problem=10
from sympy import sieve

if __name__ == "__main__":
    print(sum(sieve.primerange(1, 2e6 + 1)))
