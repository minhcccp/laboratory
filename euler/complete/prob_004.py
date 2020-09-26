# From: https://projecteuler.net/problem=4
from palindrome_checker import is_palindrome

if __name__ == "__main__":
    record: int = 0

    first: int = 999
    while first >= 100:
        if not first % 11:
            second: int = 999
            delta: int = 1

        else:
            second = 990
            delta = 11

        while second >= first:
            if (challenger := first * second) <= record:
                break

            if is_palindrome(challenger):
                record = challenger

            second -= delta

        first -= 1

    print(record)
