from typing import List

from sympy import totient
from sympy.ntheory import isprime, digits

if __name__ == "__main__":

    def digit_list(dl_number: int) -> List[int]:
        return digits(dl_number)[1:]

    def final(testee: int) -> float:
        return testee / totient(testee)

    print(
        min(
            (
                candidate
                for candidate in reversed(range(4, int(1e7)))
                if (dlc := digit_list(candidate))[0] != 1
                and not isprime(candidate)
                and sorted(dlc) == sorted(digit_list(int(totient(candidate))))
            ),
            key=final,
        )
    )
