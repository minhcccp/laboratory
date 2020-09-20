from time import time

from sympy import totient, isprime

if __name__ == "__main__":
    start = time()
    print(
        min(
            (
                (candidate / euler_func, candidate)
                for candidate in range(1 * 10 ** 5 - 1, 20, -1)
                if not isprime(candidate)
                and candidate % 100
                and sorted(str(candidate))
                == sorted(str(euler_func := totient(candidate)))
            ),
        )[1],
        time() - start,
    )
