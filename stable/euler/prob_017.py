# From:https://projecteuler.net/problem=17
from typing import Dict

from sympy.ntheory import digits

if __name__ == "__main__":

    def number_to_words(number: int) -> str:
        one_to_nine: Dict[int, str] = {
            1: "one ",
            2: "two ",
            3: "three ",
            4: "four ",
            5: "five ",
            6: "six ",
            7: "seven ",
            8: "eight ",
            9: "nine ",
        }
        ten_to_nineteen: Dict[int, str] = {
            0: "ten ",
            1: "eleven ",
            2: "twelve ",
            3: "thirteen ",
            4: "fourteen ",
            5: "fifteen ",
            6: "sixteen ",
            7: "seventeen ",
            8: "eighteen ",
            9: "nineteen ",
        }
        twenty_to_ninety: Dict[int, str] = {
            2: "twenty ",
            3: "thirty ",
            4: "forty ",
            5: "fifty ",
            6: "sixty ",
            7: "seventy ",
            8: "eighty ",
            9: "ninety ",
        }

        hundreds_digit: int
        tens_digit: int
        ones_digit: int
        hundreds_digit, tens_digit, ones_digit = digits(number, digits=3)[1:]

        result: str = ""
        if hundreds_digit:
            result += one_to_nine[hundreds_digit] + "hundred "

            if any(digit for digit in [tens_digit, ones_digit]):
                result += "and "

        if tens_digit == 1:
            result += ten_to_nineteen[ones_digit]

        else:
            if tens_digit:
                result += twenty_to_ninety[tens_digit]

            if ones_digit:
                result += one_to_nine[ones_digit]

        return result

    print(
        sum(special_char.isalpha() for special_char in "one thousand")
        + sum(
            sum(char.isalpha() for char in number_to_words(testee))
            for testee in range(1, int(1e3))
        )
    )
