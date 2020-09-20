"""
Resource(s):
https://en.wikipedia.org/wiki/Roman_numerals

"""

from timeit import timeit
from typing import Dict

from sympy.ntheory import digits


def decoder(roman: str) -> int:
    """
    :param roman: Roman number
    :return: Corresponding integer
    """

    try:
        total: int = 0

        roman_to_numeral: Dict[str, int]
        previous_value: int = (
            roman_to_numeral := (
                {
                    "M": 1000,
                    "D": 500,
                    "C": 100,
                    "L": 50,
                    "X": 10,
                    "V": 5,
                    "I": 1,
                }
            )
        )[(roman := roman.upper())[0]]

        index: int
        char: str
        for index, char in enumerate(roman[1:]):
            ratio: int
            next_value: int
            if (
                ratio := (next_value := roman_to_numeral[char]) // previous_value
            ) > 10 or (ratio == 10 and str(previous_value)[0]) == "5":
                raise ValueError(
                    f"The combination at indices {index} and {index + 1} does not exist"
                )

            if ratio > 1:
                previous_value = -previous_value

            total += previous_value
            previous_value = next_value

        return total + previous_value

    except KeyError as invalid_char_error:
        raise ValueError("Input has non Roman-numeral digits") from invalid_char_error


def encoder(decimal: int) -> str:
    """
    :param decimal: Integer, must be positive and smaller than 5,000
    :return: Corresponding Roman number
    """

    if not (0 < decimal < 5e3):
        raise ValueError("Integer must be positive and smaller than 5,000")

    return "".join(
        "MDCLXVI"[value]
        for group in (
            [index * 2, index * 2 - (digit + 1) // 5]
            if digit % 5 == 4 and index
            else (digit >= 5) * [index * 2 - 1] + (digit % 5) * [index * 2]
            if digit
            else []
            for index, digit in enumerate(digits(decimal, digits=4)[1:])
        )
        for value in group
    )


if __name__ == "__main__":
    for s in [
        "MMMDCCCLXXXVIII",
        "XLVII",
        "XCIX",
        "MMXLVIII",
        "I",
        # The following lines contain values raising exception, uncomment to see it happen
        # "VL",
        # "XM",
    ]:
        print(
            decoder(s),
            timeit('decoder(s)', globals=globals()),
            "μs",
        )

    for n in [
        99,
        2020,
        2048,
        # The following line contains value raising exception, uncomment to see it happen
        # 10000
    ]:
        print(
            encoder(n),
            timeit("encoder(n)", globals=globals()),
            "μs",
        )
