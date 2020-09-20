# From: https://en.wikipedia.org/wiki/Ackermann_function
from sys import getrecursionlimit

from numpy import long


def naive_approach(first: int, second: int) -> int:
    """


    :param first:
    :param second:
    :return:
    """

    if first < 0 or second < 0:
        raise ValueError("Neither of the inputs can be negative")

    if not first:
        return second + 1

    if not second:
        return naive_approach(first - 1, 1)

    return naive_approach(first - 1, naive_approach(first, second - 1))


if __name__ == "__main__":
    try:
        print(naive_approach(*[long(number) for number in input().split()]))
    except RecursionError:
        raise RecursionError(
            f"The function has reached the system recursion limit ({getrecursionlimit()} times)"
        )
