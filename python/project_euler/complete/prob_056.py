# From: https://projecteuler.net/problem=56
from itertools import product

from perfect_digital_invariant import pdi_function

if __name__ == "__main__":
    using_range: range = range(1, 100)
    print(
        max(
            pdi_function(base ** power)
            for base, power in product(using_range, using_range)
        )
    )
