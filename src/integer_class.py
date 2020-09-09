from typing import Union, Any

from numpy import long
from sympy import Integer

FULL_INTEGER_CLASS = Union[int, long, Integer]


def is_integer(checking_object: Any) -> bool:
    """
    :param checking_object: Object to be checked
    :return: Boolean value whether object is an integer
    """

    return isinstance(checking_object, FULL_INTEGER_CLASS.__args__)


if __name__ == "__main__":
    print(is_integer(3))
    print(is_integer(long(1e100)))
    print(is_integer(3.0))
