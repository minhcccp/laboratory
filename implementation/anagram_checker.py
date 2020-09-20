# From: https://twitter.com/fermatslibrary/status/1275066521450975234
from math import prod
from string import ascii_lowercase

from sympy import prime


def are_anagram(word_1: str, word_2: str) -> bool:
    def word_to_product(word: str) -> int:
        return prod(
            prime(ascii_lowercase.index(letter) + 1)
            for letter in word.lower()
            if letter in ascii_lowercase
        )

    return word_to_product(word_1) == word_to_product(word_2)


if __name__ == "__main__":
    print(are_anagram("Silent", "Listen"))
