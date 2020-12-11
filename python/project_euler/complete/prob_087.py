"""
From:
https://projecteuler.net/problem=87
"""
from math import ceil

from sympy import root
from sympy.ntheory import primerange


def scope(nth_root: int):
    return (_ ** nth_root for _ in primerange(2, ceil(root(limit, nth_root))))


def test(number: int) -> bool:
    return number < limit


if __name__ == "__main__":
    limit: float = 5e7
    rs: set[int] = set()
    first_number: int
    for first_number in scope(2):
        current: int = first_number

        first_flag: bool
        if first_flag := test(current):
            second_number: int
            for second_number in scope(3):
                current += second_number

                second_flag: bool
                if second_flag := test(current):
                    third_number: int
                    for third_number in scope(4):
                        current += third_number

                        third_flag: bool
                        if third_flag := test(current):
                            rs.add(current)

                        current -= third_number

                        if not third_flag:
                            break

                current -= second_number

                if not second_flag:
                    break

        current -= first_number

        if not first_flag:
            break

    print(len(rs))
