# From: https://projecteuler.net/problem=24
from itertools import permutations
from string import digits

if __name__ == "__main__":
    print("".join(list(permutations(digits))[int(1e6) - 1]))
