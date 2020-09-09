# From: https://projecteuler.net/problem=42
from string import ascii_uppercase
from typing import List

if __name__ == "__main__":
    triangle_list: List[int] = [1]
    start: int = 1
    while triangle_list[-1] < max(
        sum_equivalent := [
            sum(ascii_uppercase.index(letter) + 1 for letter in word)
            for word in open("p042_words.txt").read().replace('"', "").split(",")
        ]
    ):
        start += 1
        triangle_list.append(start * (start + 1) // 2)

    print(sum(word in triangle_list for word in sum_equivalent))
