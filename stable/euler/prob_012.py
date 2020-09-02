# From: https://projecteuler.net/problem=12
from sympy import divisor_count

if __name__ == "__main__":
    limit: int = 9
    while divisor_count(result := sum(range(limit))) <= 500:
        limit += 1

    print(result)
