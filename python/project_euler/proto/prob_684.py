"""
Resource(s):
https://projecteuler.net/problem=684

"""

from timeit import timeit


def trial(param: int) -> int:
    return param if param < 10 else int(str(param % 9) + "9" * (param // 9))


if __name__ == "__main__":
    for num in range(20):
        print(trial(num), f'{timeit("trial(num)", globals=globals())} μs', sep="\n")
