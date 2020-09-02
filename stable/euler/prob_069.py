# From: https://projecteuler.net/problem=69
from sympy import totient

if __name__ == "__main__":
    print(
        list(start_range := range(2, int(1e6 + 1)))[
            (result_list := [number / totient(number) for number in start_range]).index(
                max(result_list)
            )
        ]
    )
    pass
