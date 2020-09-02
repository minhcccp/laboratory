# From: https://projecteuler.net/problem=21
from sympy import proper_divisors

if __name__ == "__main__":

    def the_test(testee: int) -> int:
        if (result := sum(proper_divisors(testee))) > testee and sum(
            proper_divisors(result)
        ) == testee:
            return testee + result

        return 0

    print(sum(the_test(number) for number in range(2, int(1e4))))
