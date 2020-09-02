# From: https://projecteuler.net/problem=41
from string import digits

from sympy import Integer as Int
from sympy import prevprime

if __name__ == "__main__":

    def checker(checking_number: Int) -> bool:
        str_version: str = str(checking_number)

        if set(str_version) == set(digits[1 : len(str_version) + 1]):
            print(checking_number)
            return False

        return True

    # Max pandigital prime has upto 7 digits, first prime greater than 7_654_321 is stated in the variable below
    start: Int = Int(7_654_337)
    while checker(start):
        start = prevprime(start)
