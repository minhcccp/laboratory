from string import digits
from sympy import fibonacci as fib

if __name__ == "__main__":
    reference_set: set[str] = set(digits[1:])
    start: int = 2750
    while not (
        set((str_version := str(fib(start)))[:9]) == reference_set
        and set(str_version[-9:]) == reference_set
    ):
        start += 1

    print(start)
