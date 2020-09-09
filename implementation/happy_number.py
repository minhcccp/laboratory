# From: https://en.wikipedia.org/wiki/Happy_number
from typing import List, Union

from numpy import long
from sympy import Integer

from digital_function import pdi_function


def is_happy(number: Union[int, long, Integer]) -> bool:
    """
    Check if a number is happy or not

    :param number: The checking number
    :return: The boolean result
    """

    chain_list: List[int] = [number]
    while not any(critical in chain_list for critical in [1, 89]):
        chain_list.append(pdi_function(chain_list[-1], 2))

    if 1 in chain_list:
        return True

    return False
    
