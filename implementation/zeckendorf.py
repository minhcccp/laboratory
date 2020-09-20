# From: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
from itertools import compress

from fibonacci_sequence import sequence_generator
from scripts_with_inputs import quit_confirmation, QUIT_REMINDER


def decimal_to_zeckendorf(decimal: int) -> str:
    """
    :param decimal: Original positive integer
    :return: Corresponding Zeckendorf representation
    """

    if decimal < 1:
        raise ValueError("Integer must be positive")

    zeckendorf_representation: str = ""
    for base in sequence_generator(False, decimal)[::-1]:
        if decimal >= base:
            zeckendorf_representation += "1"
            decimal -= base
        else:
            zeckendorf_representation += "0"

        if not decimal:
            break

    return zeckendorf_representation


def fibonacci_to_zeckendorf(fibonacci_sequence: str) -> str:
    """
    :param fibonacci_sequence: Original Fibonacci representation
    :return: Corresponding Zeckendorf representation
    """

    if set(fibonacci_sequence).difference({"0", "1"}):
        raise ValueError("Input sequence has characters not being either 0 or 1")

    while "11" in fibonacci_sequence:
        fibonacci_sequence = ("0" + fibonacci_sequence).replace("011", "100")

    return fibonacci_sequence[fibonacci_sequence.find("1") :]


def fibonacci_to_decimal(fibonacci_sequence: str) -> int:
    """
    :param fibonacci_sequence: Original Fibonacci representation
    :return: Corresponding positive integer
    """

    return sum(
        compress(
            sequence_generator(
                True,
                len((fibonacci_sequence := fibonacci_sequence[::-1])),
                (int(value) for value in fibonacci_sequence),
            )
        )
    )


if __name__ == "__main__":
    print(
        QUIT_REMINDER,
        """\
0 - Convert a decimal to Zeckendorf representation
1 - Convert a Fibonacci representation to Zeckendorf representation
2 - Convert a Fibonacci representation to a decimal\n""",
        sep="\n",
    )

    option: int = -1
    while option not in range(3):
        try:
            option = int(
                quit_confirmation(
                    "Type the number corresponding to your chosen option: "
                )
            )

        except ValueError:
            print("Invalid option")
            continue

    if option:
        while True:
            try:
                input_value: str = quit_confirmation(
                    "Type the Fibonacci representation: "
                )

                if option == 1:
                    print(fibonacci_to_zeckendorf(input_value))

                else:
                    print(fibonacci_to_decimal(input_value))

                break

            except ValueError as invalid_char_error:
                print(invalid_char_error.message)

    else:
        while True:
            try:
                print(
                    decimal_to_zeckendorf(
                        int(quit_confirmation("Type the decimal number: "))
                    )
                )

                break

            except ValueError as invalid_char_error:
                print(invalid_char_error.message)
