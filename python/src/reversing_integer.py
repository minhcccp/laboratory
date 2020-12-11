"""
A script for a function to reverse integers

"""

from sympy.ntheory import digits


def reversal(number: int, base: int = 10) -> int:
    """
    :param number: Input number written in decimal
    :param base: Base of the input number, defaulting to be 10
    :return: Decimal value of the output
    """
    return sum(
        digit * base ** index for index, digit in enumerate(digits(number, base)[1:])
    )


if __name__ == "__main__":
    print(reversal(1234))
    print(reversal(1234, 2))
