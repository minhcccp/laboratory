# From: https://projecteuler.net/problem=43
from itertools import permutations
from string import digits

from sympy import primerange

if __name__ == "__main__":
    print(
        sum(
            int(number)
            for number in [
                "".join(combination)
                for combination in permutations(digits)
                if combination[0] != "0"
                and combination[5] in ["0", "5"]
                and not int(combination[3]) % 2
            ]
            if not any(
                int(number[index + 2 : index + 5]) % list(primerange(3, 18))[index]
                for index in range(6)
            )
        )
    )
