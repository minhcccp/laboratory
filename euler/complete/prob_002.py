# From: https://projecteuler.net/problem=2
from mpmath import fibonacci
from numpy import long

if __name__ == "__main__":
    total: long = 0
    start_index: long = 3

    while (current := long(fibonacci(start_index))) <= 4e6:
        total += current
        start_index += 3

    print(total)
