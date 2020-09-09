# From: https://en.wikipedia.org/wiki/Fibonacci_number
from typing import List

from sympy import fibonacci, Integer

from integer_class import FULL_INTEGER_CLASS


def sequence_generator(
    option: bool, detail: FULL_INTEGER_CLASS, unique_member: bool = True
) -> List[FULL_INTEGER_CLASS]:
    """
    Generate a list of Fibonacci numbers

    :param option: Working mode, either False or True, see explanation below
    :param detail: Specifying either the greatest possible value (for option False) or number of values (option True)
    :param unique_member: Default is to return nonzero unique numbers only, change to False for 0 as the starting number
    :return: The sequence satisfying the requirements
    """

    start: int = unique_member * 2

    if option:
        fibonacci_list: List[FULL_INTEGER_CLASS] = [
            Integer(fibonacci(index + start)) for index in range(detail)
        ]

    else:
        fibonacci_list = [0]

        while fibonacci_list[-1] <= detail:
            fibonacci_list.append(Integer(fibonacci(len(fibonacci_list))))

        fibonacci_list = fibonacci_list[start:-1]

    return fibonacci_list


if __name__ == "__main__":
    print(sequence_generator(False, 13))
    print(sequence_generator(False, 14))
    print(sequence_generator(True, 10))
    print(sequence_generator(True, 10, False))
