# From: https://projecteuler.net/problem=25
from sympy import fibonacci

if __name__ == "__main__":
    start: int = 12
    while len(str(fibonacci(start))) < 1e3:
        start += 1

    print(start)
