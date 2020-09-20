"""
Resource(s):
https://projecteuler.net/problem=59

"""
from itertools import cycle
from string import ascii_lowercase
from typing import List, TextIO


def converter(string: str) -> List[int]:
    return [ord(char) for char in string]


def trial():
    CONST: List[int] = converter("the")

    input_file: TextIO
    with open("prob_059.txt") as input_file:
        value: str
        encrypted_list: List[int] = [
            int(value) for value in input_file.read().split(",")
        ]

    prob = [
        result
        for start_index in range(len(encrypted_list) - 3)
        if (
            result := "".join(
                chr(first ^ second)
                for first, second in zip(
                    CONST, encrypted_list[start_index : start_index + 3]
                )
            )
        )
        and all(cha in ascii_lowercase for cha in result)
    ]

    sort = sorted(set(prob), key=prob.count, reverse=True)
    for item in sort:
        if (
            final := "".join(
                chr(f ^ s) for f, s in zip(encrypted_list, cycle(converter(item)))
            )
        ) and all(c in ascii_lowercase or c == " " for c in final):
            return final

    # print(*encrypted_list)
    # return len(encrypted_list)


if __name__ == "__main__":
    print(trial())
