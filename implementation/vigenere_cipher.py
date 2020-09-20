# From: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
from itertools import cycle
from string import ascii_lowercase as letters
from typing import List, Tuple

from scripts_with_inputs import quit_confirmation, QUIT_REMINDER

# Complimentary functions
avail_mode: List[int] = [1, -1]


def is_main() -> bool:
    """
    Return if the script is being run or only a function is called

    :return: The boolean value for the running status
    """

    return __name__ == "__main__"


def input_error(notification: str):
    """
    Raise the error while inputting data

    :param notification: The content of the error
    :return: The error and the message
    """

    raise ValueError(notification)


# Main functions
def setup(setup_mode: int = 0, setup_key: str = ""):
    """
    Set up the working option, the input message and the key
    """

    while setup_mode not in avail_mode:
        try:
            setup_mode = int(
                quit_confirmation("\nType 1 to encrypt or -1 to decrypt a message: ")
            )

        except ValueError:
            pass

    setup_key_char: str
    while not setup_key:
        setup_key = "".join(
            setup_key_char
            for setup_key_char in quit_confirmation(
                "\nType your key, which contains at least 1 English letter: "
            ).lower()
            if setup_key_char.isalpha()
        )

    main_feature(setup_mode, setup_key, quit_confirmation("\nType your input message: "))


def main_feature(main_mode: int, main_key: str, main_input: str) -> str:
    """
    The function for encryption using Vigenère cipher

    :param main_mode: The working option, must be either 1 (encrypt) or -1 (decrypt)
    :param main_input: The input message
    :param main_key: The key for the message
    :return: The output message
    """

    if not is_main():
        if main_mode not in avail_mode:
            input_error("The option must be either 1 (encrypt) or -1 (decrypt)")

        if not (
            main_key := "".join(
                main_key_char
                for main_key_char in main_key.lower()
                if main_key_char.isalpha()
            )
        ):
            input_error("The key should have at least 1 English letter")

    letter_pair: Tuple[int, int]
    main_input_char: str
    main_key_letter: str
    main_output_list: List[str] = [
        letters[sum(letter_pair) % 26]
        for letter_pair in zip(
            [
                letters.index(main_input_char)
                for main_input_char in main_input.lower()
                if main_input_char.isalpha()
            ],
            cycle(
                letters.index(main_key_letter) * main_mode
                for main_key_letter in main_key
            ),
        )
    ]

    index: int
    char: str
    for index, char in enumerate(main_input):
        if not char.isalpha():
            main_output_list.insert(index, char)
        elif char.isupper():
            main_output_list[index] = main_output_list[index].upper()

    main_output_str: str = "".join(main_output_list)

    if is_main():
        result(main_key, main_input, main_output_str)
    else:
        return main_output_str


def result(result_key: str, result_input: str, result_output: str) -> None:
    """
    Print out the result and save any data if needed

    :param result_input: The input message
    :param result_key: The formatted key for the input message
    :param result_output: The output message
    """

    print(f"\nYour output message is:\n{result_output}")

    if (
        result_numbers := quit_confirmation(
            "\nTo save any of the key (0), the input message (1) or the output message (2) to a .txt file, "
            "type the corresponding numbers, or press enter if not: "
        )
    ) :
        result_pair_list = [
            ["key", result_key],
            ["input message", result_input],
            ["output message", result_output],
        ]

        with open("Cipher_result.txt", "a") as result_file:
            result_file.writelines(
                [
                    f"The {result_pair_list[int(index)][0]} is: {result_pair_list[int(index)][1]}"
                    for index in result_numbers
                ]
                + ["\n"]
            )

        print("Result saved!")

    quit_confirmation("Type 'quit' to stop the program, or press enter to current again: ")
    setup()


if is_main():
    print("This program is for English paragraph only", QUIT_REMINDER, sep="\n")
    setup()
