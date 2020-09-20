"""
Resource(s):
https://en.wikipedia.org/wiki/Palindrome

"""

from typing import Union

from sympy.ntheory import is_palindromic


def is_palindrome(input_data: Union[int, str], number_base: int = 0) -> bool:
    """
    :param input_data: Object to be checked, must be either a string or an integer
    :param number_base: Default is 0 (i.e. the object is a str), value must be changed if the object is an integer
    :return: Boolean result whether the object is palindromic
    """

    if isinstance(input_data, int):
        if number_base < 1:
            raise Exception(
                "number_base cannot be smaller than 1 if input_data is an int"
            )

        return is_palindromic(input_data, number_base)

    else:
        if number_base:
            raise Exception("number_base must be 0 if input_data is a str")

        return input_data == input_data[::-1]


if __name__ == "__main__":
    print(is_palindrome(1234321, 10))
    print(is_palindrome("abcba"))
