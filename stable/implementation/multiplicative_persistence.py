# From: https://en.wikipedia.org/wiki/Persistence_of_a_number

from numpy import long
from sympy import prod
from sympy.ntheory import digits


def persistence(checking_number: long, total_times: long = 0) -> long:
    """
    Return the multiplicative persistence of a given number

    :param checking_number: The number whose multiplicative persistence to be found
    :param total_times: Number of multiplication rounds, no need to be filled in
    :return: The multiplicative persistence
    """

    if len(digit_list := digits(checking_number)[1:]) < 2:
        return total_times

    if 0 in digit_list:
        return total_times + 1

    if 5 in digit_list and any(not digit % 2 for digit in digit_list):
        return total_times + 2

    return persistence(prod(digit_list), total_times + 1)


if __name__ == "__main__":
    record: long = -1
    checking_num: long = 0

    while record < 10:
        if (current := persistence(checking_num)) > record:
            print(checking_num, current)
            record = current

        checking_num += 1
