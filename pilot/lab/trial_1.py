from fractions import Fraction
from math import prod, modf
from time import time  # Must be included

from sympy import totient
from sympy.ntheory import primefactors

if __name__ == "__main__":
    const: int = 123_456_789_012_345_678_901_234_567_890

    def print_time() -> float:
        return modf(time())[0]

    start: float = print_time()
    print(const / totient(const))
    print(abs(start - (start := print_time())))

    print(prod(1 + 1 / (prime - 1) for prime in primefactors(const)))
    print(abs(start - (start := print_time())))

    print(float(prod(Fraction(prime, prime - 1) for prime in primefactors(const))))
    print(abs(start - (start := print_time())))

    pass
