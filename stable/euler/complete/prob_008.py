# From: https://projecteuler.net/problem=8
from typing import List

from numpy import long
from sympy import prod
from sympy.ntheory import digits

if __name__ == "__main__":
    digit_list: List[int] = digits(
        long(open("p008_number.txt").read().replace("\n", ""))
    )[1:]

    print(
        max(
            prod(digit_list[start_index : start_index + 13])
            for start_index in range(len(digit_list))
        )
    )
