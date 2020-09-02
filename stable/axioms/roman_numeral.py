# From: https://en.wikipedia.org/wiki/Roman_numerals
from typing import List, Union

from bidict import bidict
from sympy.ntheory import digits

reference: bidict[str, int] = bidict(
    {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
)


def roman_decoder(roman: str) -> Union[int, str]:
    """
    :param roman: Roman number
    :return: The corresponding decimal integer
    """

    try:
        symbol: str
        corresponding_values: List[int] = [
            reference[symbol] for symbol in roman.upper()
        ]

        index: int
        unsigned_value: int
        for index, unsigned_value in enumerate(corresponding_values[:-1]):
            corresponding_values[index] = unsigned_value * (-1) ** (
                unsigned_value < corresponding_values[index + 1]
            )
        return sum(corresponding_values)

    except KeyError:
        raise Exception("Input has non Roman-numeral digits")


def roman_encoder(decimal: int) -> str:
    """
    :param decimal: Decimal integer, must be in the exclusive range of 0 and 4e3
    :return: The corresponding Roman number
    """

    if not (0 < decimal < 4e3):
        raise ValueError("Integer must be positive and smaller than 4,000")

    return "".join(
        reference.inverse.get(value, "")
        for group in reversed(
            [
                [10 ** index, (digit + 1) * 10 ** index]
                if digit % 5 == 4
                else [(digit // 5) * 5 * 10 ** index] + [10 ** index] * (digit % 5)
                if digit
                else [0]
                for index, digit in enumerate(reversed(digits(decimal)[1:]))
            ]
        )
        for value in group
    )


if __name__ == "__main__":
    for s in ["MMMDCCCLXXXVIII", "MMDCCCLXXXVIII", "XCIX", "MMXLVIII"]:
        print(len(s), roman_decoder(s))

    for n in [99, 2020, 2048, 10000]:
        print(n, roman_encoder(n))
