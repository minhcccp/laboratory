# From: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
from itertools import cycle
from string import ascii_lowercase as letters
from typing import List


def vigenere_function(input_message: str, key: str, decode_mode: bool = False) -> str:
    input_letter: int
    key_letter: int
    input_char: str
    key_char: str
    proto_output: List[str] = [
        letters[(input_letter + key_letter * (-1) ** decode_mode) % len(letters)]
        for input_letter, key_letter in zip(
            (
                letters.index(input_char)
                for input_char in input_message.lower()
                if input_char.isalpha()
            ),
            cycle(
                letters.index(key_char)
                for key_char in key.lower()
                if key_char.isalpha()
            ),
        )
    ]

    pointer: int
    value: str
    for pointer, value in enumerate(input_message):
        if not value.isalpha():
            proto_output.insert(pointer, value)
        elif value.isupper():
            proto_output[pointer] = proto_output[pointer].upper()

    return "".join(proto_output)


if __name__ == "__main__":
    print(vigenere_function("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR")
