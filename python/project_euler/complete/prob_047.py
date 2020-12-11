# From: https://projecteuler.net/problem=47
from sympy import primefactors

if __name__ == "__main__":
    start: int = 210
    while not all(
        current := [
            len(primefactors(number)) == 4 for number in range(start, start + 4)
        ]
    ):
        try:
            if custom_increment := current.index(True, 1):
                start += custom_increment

        except ValueError:
            start += 4

    print(start)
