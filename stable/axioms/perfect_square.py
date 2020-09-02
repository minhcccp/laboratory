# From: https://en.wikipedia.org/wiki/Square_number
from math import isqrt

from integer_class import FULL_INTEGER_CLASS


def is_square(number: FULL_INTEGER_CLASS) -> bool:
    """
    Return whether a non-negative integer is a perfect square number

    :param number: The checked number
    :return: Boolean result whether the number is a perfect square
    """

    if number < 0:
        raise ValueError("Number must not be negative")

    return number == isqrt(number) ** 2


if __name__ == "__main__":
    for num in range(100):
        print(num, is_square(num))
