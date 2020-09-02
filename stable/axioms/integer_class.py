from typing import Union

from numpy import long
from sympy import Integer

FULL_INTEGER_CLASS = Union[int, long, Integer]

if __name__ == "__main__":
    print(isinstance(3, FULL_INTEGER_CLASS.__args__))
    print(isinstance(long(1e100), FULL_INTEGER_CLASS.__args__))
    print(isinstance(3.0, FULL_INTEGER_CLASS.__args__))
