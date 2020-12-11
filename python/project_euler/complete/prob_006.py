# From: https://projecteuler.net/problem=6
from sympy import summation
from sympy.abc import n

if __name__ == "__main__":
    print(summation(n, (n, 1, 20)) ** 2 - summation(n ** 2, (n, 1, 20)))
