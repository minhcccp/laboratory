# From: https://projecteuler.net/problem=65
from fractions import Fraction as Frac
from typing import List

from sympy.ntheory import digits

if __name__ == "__main__":
    number_of_convergent: int = 100

    convergent_list: List[int] = [2]
    for next_index in range(2, number_of_convergent + 1):
        convergent_list.append(1 if next_index % 3 else 2 * next_index // 3)

    result: Frac = Frac(1, convergent_list.pop())
    for next_number in reversed(convergent_list):
        result = next_number + 1 / result

    print(sum(digits(result.numerator)[1:]))
