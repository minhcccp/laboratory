# From: https://projecteuler.net/problem=206
from string import digits

if __name__ == "__main__":
    start: int = 100_000_003
    while str(start ** 2)[::2] != digits[1:]:
        start += 4 if start % 10 == 3 else 6

    print(start * 10)
