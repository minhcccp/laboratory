# From: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
from numpy import sum, long

from fibonacci_sequence import sequence_generator
from script_quit import quit_confirmation, QUIT_REMINDER


def decimal_to_zeckendorf(decimal: long) -> str:
    """
    Conversion from a decimal to its corresponding Zeckendorf representation

    :param decimal: The original decimal
    :return: The Zeckendorf representation
    """

    zeckendorf_representation: str = ""
    for base in sequence_generator(False, decimal)[::-1]:
        if decimal > base:
            zeckendorf_representation += "1"
            decimal -= base

        else:
            zeckendorf_representation += "0"

    return zeckendorf_representation


def fibonacci_to_zeckendorf(fibonacci_sequence: str) -> str:
    """
    Conversion from a Fibonacci representation to its corresponding Zeckendorf one

    :param fibonacci_sequence: The original Fibonacci representation
    :return:The Zeckendorf representation
    """

    while "11" in fibonacci_sequence:
        fibonacci_sequence = ("0" + fibonacci_sequence).replace("011", "100")

    return fibonacci_sequence[fibonacci_sequence.find("1") :]


def fibonacci_to_decimal(fibonacci_sequence: str) -> long:
    """
    Conversion from a Fibonacci representation to its corresponding decimal

    :param fibonacci_sequence: The original Fibonacci representation
    :return: The decimal
    """

    return long(
        sum(
            sequence_generator(
                True, len((fibonacci_sequence := fibonacci_sequence[::-1]))
            ),
            where=[long(digit) for digit in fibonacci_sequence],
        )
    )


if __name__ == "__main__":
    print(QUIT_REMINDER)

    option: long = -1
    while option not in range(3):
        try:
            option = long(
                quit_confirmation(
                    """0 - Convert a decimal to Zeckendorf representation
1 - Convert a Fibonacci representation to Zeckendorf representation
2 - Convert a Fibonacci representation to a decimal
Type the number corresponding to your chosen option: """
                )
            )
        except ValueError:
            continue

    if option:
        input_value: str = "a"
        while (not input_value) or (
            any(digit not in ["0", "1"] for digit in input_value)
        ):
            input_value = quit_confirmation("Type the Fibonacci representation: ")

        if option == 1:
            print(fibonacci_to_zeckendorf(input_value))

        if option == 2:
            print(fibonacci_to_decimal(input_value))

    else:
        while True:
            try:
                print(decimal_to_zeckendorf(long(quit_confirmation("Type the decimal number: "))))
                break

            except ValueError:
                continue
