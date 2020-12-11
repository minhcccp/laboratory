# From: https://projecteuler.net/problem=357
from typing import List

from numpy import sum
from sympy import divisors, isprime, primerange, sqrt

if __name__ == "__main__":

    def the_purge(purgee: int) -> bool:
        return not purgee % 10 in [4, 6] and (
            # all(
            #     purgee % (prime ** 2) and not purgee % prime == prime - 1
            #     for prime in primerange(3, sqrt(purgee / 2) + 1)
            # )
        )

    def the_main_test(testee: int) -> bool:
        def get_half(input_list: List[int]) -> List[int]:
            return input_list[: len(input_list) // 2]

        return all(
            isprime(divisor + testee // divisor)
            for divisor in get_half(divisors(testee))
        )

    record: List[int] = [1, 2, 6]
    for tester in range(10, int("9" * 8), 4):
        if the_purge(tester):
            print(tester, (result := the_main_test(tester)))

            if result:
                record.append(tester)

    with open("prob_357_proto.txt", "a") as result_trial:
        result_trial.writelines([str(item) + "\n" for item in record])

    print(sum(record))

    # print(sum(record + [tester for tester in range(10, int("9" * 8), 4) if the_purge(tester) and the_main_test(
    # tester)]))
