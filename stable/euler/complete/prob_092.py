# From: https://projecteuler.net/problem=92
from itertools import combinations_with_replacement, permutations
from string import digits
from typing import List, Set

from digital_function import pdi_function

if __name__ == "__main__":
    one_set: Set[str] = {"1"}
    eighty_nine_set: Set[str] = {"89"}

    start_number: str
    for start_number in reversed(
        [
            "".join(possibility)
            for length in range(1, 8)
            for possibility in combinations_with_replacement(digits[1:], length)
        ]
    ):
        if start_number not in one_set | eighty_nine_set:

            class Collection:
                ledger: List[str]

                def __init__(self, first_num: str):
                    self.ledger = [first_num]
                    self.next_item()

                def last_item(self):
                    return self.ledger[-1]

                def next_item(self):
                    self.ledger.append(
                        "".join(
                            sorted(
                                str(
                                    pdi_function(
                                        int(self.last_item()), 2
                                    )
                                ).replace("0", "")
                            )
                        )
                    )

                def return_ledger(self):
                    return self.ledger

            new_collection: Collection = Collection(start_number)
            while not (
                (trace := new_collection.last_item() in eighty_nine_set)
                or new_collection.last_item() in one_set
            ):
                new_collection.next_item()

            if trace:
                eighty_nine_set.update(new_collection.return_ledger())
            else:
                one_set.update(new_collection.return_ledger())

    print(
        sum(
            len(
                {
                    "".join(item)
                    for item in permutations(number + "0" * (7 - len(number)))
                }
            )
            for number in eighty_nine_set
        )
    )
