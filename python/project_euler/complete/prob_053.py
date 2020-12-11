"""
From:
https://projecteuler.net/problem=53
"""

from sympy.ntheory import binomial_coefficients_list as bcl

if __name__ == "__main__":
    print(
        sum(sum(element > 1e6 for element in bcl(number)) for number in range(23, 101))
    )
