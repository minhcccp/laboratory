"""
Resource(s):
https://en.wikipedia.org/wiki/Perfect_digital_invariant
https://en.wikipedia.org/wiki/Digit_sum

"""

from typing import Union

from sympy.ntheory import digits


def pdi_function(input_integer: Union[int, str], power: int = 1) -> int:
    """
    :param input_integer: Integer whose digits to be calculated
    :param power: Power to which the digits are raised, default is 1 (i.e. digital sum)
    :return: Result of the perfect digital invariant function
    """

    try:
        return sum(
            pow(digit, power)
            for digit in digits(
                input_integer if isinstance(input_integer, int) else int(input_integer)
            )[1:]
        )

    except ValueError as result_error:
        raise ValueError("Only decimal digits are accepted") from result_error


if __name__ == "__main__":
    for index, trial in enumerate([1234, "1234", "123a"]):
        print(pdi_function(trial, index + 1))
