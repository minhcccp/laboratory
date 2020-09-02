# From: https://projecteuler.net/problem=35
from sympy import sieve, isprime
from sympy.ntheory import digits

if __name__ == "__main__":

    def the_test(input_number: int) -> bool:
        if input_number < 10:
            return True

        str_version: str = str(input_number)
        return all(
            digit % 2 and digit % 5 for digit in digits(input_number)[1:]
        ) and all(
            isprime(int(str_version[start_index:] + str_version[:start_index]))
            for start_index in range(1, len(str_version))
        )

    print(sum(the_test(prime) for prime in sieve.primerange(2, 1e6)))
