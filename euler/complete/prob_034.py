# From: https://projecteuler.net/problem=34

from sympy import factorial
from sympy.ntheory import digits

if __name__ == "__main__":
    print(
        sum(
            number
            for number in range(10, int(1e7))
            if number == sum(factorial(digit) for digit in digits(number)[1:])
        )
    )
