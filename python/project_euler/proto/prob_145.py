"""
From:
https://projecteuler.net/problem=145
"""

from sympy.ntheory import digits

if __name__ == "__main__":
    limit: int = 7
    result_set: set[int] = set()

    for candidate in range(21, 10 ** limit - 10 ** (limit - 1), 2):
        digit_list: list[int]
        if (
            candidate not in result_set
            and ((digit_list := digits(candidate)[1:])[0] + digit_list[-1]) % 2
        ):
            reversal: int = sum(
                digit * 10 ** index for index, digit in enumerate(digit_list)
            )
            if all(new_digit % 2 for new_digit in digits(candidate + reversal)[1:]):
                result_set.update([candidate, reversal])

    # temp: list[int] = sorted(result_set)
