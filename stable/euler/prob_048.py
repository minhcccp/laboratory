# From: https://projecteuler.net/problem=48
from sympy import summation
from sympy.abc import i

if __name__ == "__main__":
    print(str(summation(i ** i, (i, 1, 1_000)))[-10:])
