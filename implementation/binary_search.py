from typing import List

from numpy import long


def is_found(looking_list: List[long], looking_number: long) -> bool:
    """
    Check if a given number is in a given list using binary search

    :param looking_list: The given list, must be sorted beforehand, long int only
    :param looking_number: The looking int
    :return: The boolean value if the number is in the list
    """

    if looking_list[(middle_index := len(looking_list) // 2)] == looking_number:
        return True

    elif len(looking_list) == 1:
        return False

    elif looking_list[middle_index] < looking_number:
        looking_list = looking_list[middle_index + 1 :]

    else:
        looking_list = looking_list[:middle_index]

    return is_found(looking_list, looking_number)


if __name__ == "__main__":
    print(is_found([1, 3, 5, 30, 42, 43, 500], 9))
