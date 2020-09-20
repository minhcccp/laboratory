# From: https://projecteuler.net/problem=73
from itertools import combinations

from sympy import igcd, Rational

if __name__ == "__main__":
    print(
        (
            ordered_list := sorted(
                Rational(numerator, denominator)
                for numerator, denominator in combinations(range(1, int(1.2e4) + 1), 2)
                if igcd(numerator, denominator) == 1
            )
        ).index(Rational(1, 2))
        - ordered_list.index(Rational(1, 3))
        - 1
    )
