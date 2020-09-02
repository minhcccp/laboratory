# From: https://projecteuler.net/problem=71
from itertools import combinations

from sympy import igcd, Rational

if __name__ == "__main__":
    print(
        (
            ordered_list := sorted(
                Rational(numerator, denominator)
                for numerator, denominator in combinations(range(1, int(1e6) + 1), 2)
                if igcd(numerator, denominator) == 1
            )
        )[ordered_list.index(Rational(3, 7)) - 1].numerator()
    )
