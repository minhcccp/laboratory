# From: https://projecteuler.net/problem=40
from sympy import prod

if __name__ == "__main__":
    start: str = "0"
    next_number: int = 1
    while len(start) <= 1e6:
        start += str(next_number)
        next_number += 1

    print(prod(int(start[10 ** power]) for power in range(7)))
