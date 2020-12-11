from fractions import Fraction as Fra
from math import floor, gcd

from sympy import isprime as isp


def the_algorithm(current: Fra, max_no_of_digits: int) -> Fra:
    const: Fra = Fra(3, 7)

    den: int
    for den in range(10 ** (max_no_of_digits - 1), 10 ** max_no_of_digits):

        num: int = floor(den * const)
        contender: Fra
        if (isp(den) or gcd(den, num) == 1) and current < (
            contender := Fra(num, den)
        ) < const:
            current = contender

    return current


if __name__ == "__main__":
    limit: int = 6

    record: Fra = Fra()
    num_of_digits: int
    for num_of_digits in range(1, limit + 1):
        record = the_algorithm(record, num_of_digits)

    print(record)
