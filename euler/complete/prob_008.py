# From: https://projecteuler.net/problem=8
from math import prod
from typing import List

from sympy.ntheory import digits

if __name__ == "__main__":
    with open("p008_number.txt") as input_txt:
        digit_list: List[int] = digits(int(input_txt.read().replace("\n", "")))[1:]

    print(
        max(
            prod(digit_list[start_index : start_index + 13])
            for start_index in range(len(digit_list) - 13)
        )
    )
