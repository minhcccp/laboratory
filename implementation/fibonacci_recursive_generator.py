# Also include e.g. of using timeit lib, find out more at: https://realpython.com/python-timer/#estimating-running-time-with-timeit
from timeit import timeit

if __name__ == "__main__":

    def fibonacci(index: int) -> int:
        return index if index < 2 else fibonacci(index - 1) + fibonacci(index - 2)

    print(fibonacci(10), timeit("fibonacci(10)", globals=globals()))
