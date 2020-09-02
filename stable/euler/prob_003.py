# From: https://projecteuler.net/problem=3
from sympy import primefactors

if __name__ == "__main__":
    print(primefactors(600851475143)[-1])
