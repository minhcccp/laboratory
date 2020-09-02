# From: https://projecteuler.net/problem=57
from fractions import Fraction as frac

from numpy import long

if __name__ == "__main__":

    def convergent_fraction_checker(number_of_iterations: long) -> bool:
        result: frac = frac(2)
        for time in range(number_of_iterations - 1):
            result = 2 + 1 / result

        return len(str((final := 1 + 1 / result).numerator)) > len(
            str(final.denominator)
        )

    print(sum(convergent_fraction_checker(iteration) for iteration in range(1, 1_001)))
