# From: https://projecteuler.net/problem=2
from sympy import fibonacci

if __name__ == "__main__":
    total: int = 0
    start_index: int = 3

    while (current := fibonacci(start_index)) <= 4e6:
        total += current
        start_index += 3

    print(total)
