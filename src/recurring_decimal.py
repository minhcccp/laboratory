# From: https://en.wikipedia.org/wiki/Repeating_decimal
from array import array
from typing import Any, Union

from sympy import primefactors, divisors

from integer_class import FULL_INTEGER_CLASS


def repetend_length(denominator: FULL_INTEGER_CLASS) -> FULL_INTEGER_CLASS:
    """
    Return the length of the repetend (a.k.a the infinitely repeated digit sequence)

    :param denominator: The fraction's denominator, ValueError is raised if the denominator's modulus is less than 2
    :return: The repetend's length of the fraction's decimal representation
    """

    if abs(denominator) < 2:
        raise ValueError("The modulus of the denominator must be greater than 1")

    try:
        value: int
        max_prime_factor: int
        prime_factor: int
        for value in divisors(
            (
                max_prime_factor := [
                    prime_factor
                    for prime_factor in primefactors(denominator)
                    if prime_factor not in [2, 5]
                ][-1]
            )
            - 1
        ):
            if 10 ** value % max_prime_factor == 1:
                return value

    except IndexError:
        return 0


if __name__ == "__main__":
    for number in range(2, 50):
        print(number, repetend_length(number))

    print(repetend_length(67))
