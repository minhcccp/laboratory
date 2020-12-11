# From: https://projecteuler.net/problem=52
from sympy.ntheory import digits

if __name__ == "__main__":
    start: int = 54

    def the_test(input_number: int) -> bool:
        return (
            set(digits(2 * input_number))
            == set(digits(3 * input_number))
            == set(digits(4 * input_number))
            == set(digits(5 * input_number))
            == set(digits(6 * input_number))
        )

    while not the_test(start):
        start += 9

    print(start)
