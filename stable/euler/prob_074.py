# From: https://projecteuler.net/problem=74
from typing import List, Dict

from sympy import factorial
from sympy.ntheory import digits

if __name__ == "__main__":
    record_dict: Dict[int, int] = {number: 0 for number in reversed(range(int(1e6)))}
    for key in record_dict:
        if not record_dict[key]:
            ledger: List[int] = [key]

            while not (
                ledger[-1] in ledger[:-1]
                or (additional_record := record_dict.get(ledger[-1], 0))
            ):
                ledger.append(sum(factorial(digit) for digit in digits(ledger[-1])[1:]))

            ledger.pop()

            for index, result in enumerate(ledger):
                if result in record_dict:
                    record_dict[result] = len(ledger[index:]) + additional_record

    print(sum(value == 60 for value in record_dict.values()))
