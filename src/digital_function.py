"""
From:
https://en.wikipedia.org/wiki/Perfect_digital_invariant
https://en.wikipedia.org/wiki/Digit_sum
"""
from typing import Union

from sympy.ntheory import digits

from integer_class import FULL_INTEGER_CLASS


def pdi_function(
    input_integer: Union[FULL_INTEGER_CLASS, str], power: FULL_INTEGER_CLASS = 1
) -> FULL_INTEGER_CLASS:
    """
    Return the result of the perfect digital invariant function for numbers in base 10

    :param input_integer: The integer whose digits to be calculated
    :param power: The power to which the digits are raised, default is 1 (i.e. digital sum)
    :return: The final result
    """

    if isinstance(input_integer, str):
        return sum(int(digit) ** power for digit in input_integer)

    return sum(digit ** power for digit in digits(input_integer)[1:])
