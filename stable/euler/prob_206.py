# From: https://projecteuler.net/problem=206
from string import digits

from numpy import long

if __name__ == "__main__":
    start: long = 101_010_103
    while str(start ** 2)[::2] != digits[1:]:
        if start % 10 == 3:
            start += 4
        elif start % 10 == 7:
            start += 6

    print(start * 10)
