"""
Resource(s):
https://en.wikipedia.org/wiki/Fibonacci_number

"""

from sympy import fibonacci


def sequence_generator(
    option: bool, detail: int, unique_member: bool = True
) -> list[int]:

    """
    Generates the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21,...

    Parameters
    ----------
    option : bool
        A flag used to specify whether number of items (True) or max value of the list (False) would be used to define the list
    detail : int
        Argument to determine the number of items (True) or max value of the list (False)
    unique_member : bool, optional
        A flag used to specify whether the return list has unique numbers only, by default True

    Returns
    -------
    list[int]
        The list of numbers in the Fibonacci sequence satisfying the parameters
    """

    start: int = unique_member * 2

    fibonacci_list: list[int] = (
        [int(fibonacci(index + start)) for index in range(detail)] if option else [0]
    )

    if not option:
        last_item: int
        while (last_item := fibonacci_list[-1]) < detail:
            fibonacci_list.append(int(fibonacci(len(fibonacci_list))))

        fibonacci_list = fibonacci_list[start : (-1 if last_item > detail else None)]

    return fibonacci_list


if __name__ == "__main__":
    for limit in range(12, 15):
        print(sequence_generator(False, limit, bool(limit % 2)))

    for truthiness in range(2):
        print(sequence_generator(True, 10, bool(truthiness)))
