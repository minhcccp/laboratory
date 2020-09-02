# From: https://projecteuler.net/problem=65
from fractions import Fraction as frac
from typing import List

from numpy import long

if __name__ == "__main__":
    number_of_convergent: long = 100
    convergent_list: List[long] = [2]
    for next_index in range(2, number_of_convergent + 1):
        if next_index % 3:
            convergent_list.append(1)
        else:
            convergent_list.append(2 * next_index // 3)

    result: frac = frac(1, convergent_list.pop())
    for next_number in reversed(convergent_list):
        result = next_number + 1 / result

    print(sum(long(digit) for digit in str(result.numerator)))
