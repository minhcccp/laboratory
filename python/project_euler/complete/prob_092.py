"""
Resource(s):
https://projecteuler.net/problem=92

"""

from itertools import combinations_with_replacement, permutations
from string import digits
from typing import Set, Tuple

from perfect_digital_invariant import pdi_function


def chain_generator(
    first_number: str, reference_set: Set[str] = None
) -> Tuple[Set[str], str]:
    if not reference_set:
        reference_set = {first_number}
    return_set: Set[str] = {first_number}
    latest_value: str = first_number

    while (
        next_number := "".join(
            sorted(str(pdi_function(latest_value, 2)).replace("0", ""))
        )
    ) not in reference_set:
        return_set.add(latest_value := next_number)

    return return_set, next_number


if __name__ == "__main__":
    one: Set[str] = chain_generator("1")[0]
    eighty_nine: Set[str] = chain_generator("89")[0]

    length: int
    possibility: Tuple[str]
    start_number: str
    for start_number in (
        "".join(possibility)
        for length in range(7, 0, -1)
        for possibility in combinations_with_replacement(digits[1:], length)
    ):
        union: Set[str]
        if start_number not in (union := one.union(eighty_nine)):
            record: Set[str]
            hint: str
            record, hint = chain_generator(start_number, union)

            if hint in one:
                one.update(record)
            else:
                eighty_nine.update(record)

    print(
        sum(
            len(
                {
                    "".join(item)
                    for item in permutations(number + "0" * (7 - len(number)))
                }
            )
            for number in eighty_nine
        )
    )
