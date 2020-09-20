# From: https://projecteuler.net/problem=112
from typing import List

from sympy.ntheory import digits

if __name__ == "__main__":

    def bouncy_checker(testee: int) -> bool:
        digit_list: List[int] = digits(testee)[1:]
        difference_list: List[int] = [
            second - first for second, first in zip(digit_list[1:], digit_list[:-1])
        ]

        return (
            False
            if all(positive_difference >= 0 for positive_difference in difference_list)
            or all(negative_difference <= 0 for negative_difference in difference_list)
            else True
        )

    total_count: int = 1
    bouncy_count: int = bouncy_checker(total_count)

    while bouncy_count / total_count != 0.99:
        total_count += 1
        bouncy_count += bouncy_checker(total_count)

    print(total_count)
