# From: https://projecteuler.net/problem=31
from itertools import combinations_with_replacement as cwr

if __name__ == "__main__":
    print(
        [
            sum(
                [
                    sum(possibility) == 200
                    for possibility in cwr([1, 2, 5, 10, 20, 50, 100, 200], length)
                ]
            )
            for length in range(1, 201)
        ]
    )
