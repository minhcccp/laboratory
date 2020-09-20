"""
Resource(s):
https://en.wikipedia.org/wiki/Fibonacci_number

"""

from typing import List

from sympy import fibonacci


def sequence_generator(
    option: bool, detail: int, unique_member: bool = True
) -> List[int]:
    """
    :param option: Working mode, either False or True, see explanation below
    :param detail: Either the greatest possible value (for option False) or number of values (option True)
    :param unique_member: Default return nonzero unique numbers only (option True), change to False for starting from 0
    :return: Sequence of Fibonacci numbers satisfying the requirements
    """

    start: int = unique_member * 2

    if option:
        fibonacci_list: List[int] = [
            int(fibonacci(index + start)) for index in range(detail)
        ]

    else:
        fibonacci_list = [0]

        while (last_item := fibonacci_list[-1]) < detail:
            fibonacci_list.append(int(fibonacci(len(fibonacci_list))))

        fibonacci_list = fibonacci_list[start : (-1 if last_item > detail else None)]

    return fibonacci_list


if __name__ == "__main__":
    for limit in range(12, 15):
        print(sequence_generator(False, limit, bool(limit % 2)))

    for truthiness in range(2):
        print(sequence_generator(True, 10, bool(truthiness)))
