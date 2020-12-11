# From: https://projecteuler.net/problem=57
from fractions import Fraction as Frac

if __name__ == "__main__":

    result: Frac = Frac(1)
    total: int = 0
    for time in range(1_000):
        total += len(str((result := 1 + 1 / (1 + result)).numerator)) > len(
            str(result.denominator)
        )

    print(total)
