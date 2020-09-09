# From: https://projecteuler.net/problem=38
from string import digits as d_s
from time import time

from sympy.ntheory import digits as d_l_g

if __name__ == "__main__":

    def function(number: int) -> int:
        result: str = ""
        multiplier: int = 1
        while len(result) < 9:
            result += str(number * multiplier)
            multiplier += 1

        return [0, int(result)][d_s[1:] == "".join(sorted(result))]

    start = time()
    print(
        max(
            (f_r, num)
            for num in range(1, 10 ** 4)
            if not (
                0 in (d_l := d_l_g(num)[1:])
                or d_l[-1] == 5
                or ((f_r := function(num)) == 0)
            )
        )
    )
    print(time() - start)
