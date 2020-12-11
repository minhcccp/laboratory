"""
From:
https://projecteuler.net/problem=66
"""
from math import sqrt


from sympy.ntheory.primetest import is_square as isq

if __name__ == "__main__":
    result_dict: dict[int, float] = {}
    included_limit: int = 2 * 10 ** 1
    for D in range(2, included_limit + 1):
        if not isq(D):
            y: int = 1

            x_sqr: int
            while not isq(x_sqr := D * y ** 2 + 1):
                y += 1

            result_dict[D] = sqrt(x_sqr)

    print(max(result_dict, key=result_dict.get))
