# From: https://en.wikipedia.org/wiki/Palindrome
from typing import Any, Iterable, Dict


def is_palindrome(input_data: Any) -> bool:
    """
    Check if the checking_object is palindrome

    :param input_data: Object to be checked, TypeError will be raised if dictionary is passed into the function
    :return: The boolean result
    """

    if isinstance(input_data, (Dict,)):
        raise TypeError

    if isinstance(input_data, Iterable):
        return (list_version := list(input_data)) == list_version[::-1]
    else:
        return (str_version := str(input_data)) == str_version[::-1]


if __name__ == "__main__":
    print(is_palindrome(1234321))
    print(is_palindrome(["a", "b", "c", "b", "a"]))
