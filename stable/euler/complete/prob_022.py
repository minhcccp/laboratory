# From: https://projecteuler.net/problem=22
from string import ascii_uppercase

from numpy import sum

if __name__ == "__main__":
    print(
        sum(
            [
                (index + 1)
                * sum([ascii_uppercase.index(letter) + 1 for letter in word])
                for index, word in enumerate(
                    sorted(open("p022_names.txt").read().replace('"', "").split(","))
                )
            ]
        )
    )
