# From: https://en.wikipedia.org/wiki/Morse_code
from string import ascii_lowercase


def morse_func(func_input: str, is_separated: bool = True) -> str:
    """
    Return Morse representation of an English word

    :param func_input: The word to be encoded, must contain only English lowercase letter
    :param is_separated: Default will add spaces between letters, no space if it is False
    :return: The result representation
    """

    if any(letter not in ascii_lowercase for letter in func_input):
        raise ValueError("Input has non-letter characters")

    separate_char: str = " "
    if not is_separated:
        separate_char = ""

    return separate_char.join(
        ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()[
            ascii_lowercase.index(letter)
        ]
        for letter in func_input
    )


if __name__ == "__main__":
    print(morse_func("where"))
    print(morse_func("bits", False))
    print(morse_func("three", False))
