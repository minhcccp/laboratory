# From: https://projecteuler.net/problem=36
from sympy.ntheory import digits

from palindrome_checker import is_palindrome

if __name__ == "__main__":
    print(
        sum(
            number
            for number in range(int(1e6))
            if is_palindrome(digits(number)[1:])
            and is_palindrome(digits(number, 2)[1:])
        )
    )
    pass
