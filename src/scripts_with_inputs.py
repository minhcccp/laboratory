"""
A script containing useful constants and functions to be used for scripts with user inputs

"""

from sys import exit
from time import sleep

QUIT_REMINDER: str = "Type 'quit' at any time to stop the program\n"


def stop_with_goodbye() -> None:
    """
    Print the farewell statement before stopping the program
    """

    print("Thanks for using the program, see ya! From MinhCCCP")
    sleep(10)
    exit()


def quit_confirmation(question: str) -> str:
    """
    :param question: Prompt itself
    :return: Answer for the prompt if it's not "quit", else the program will be stopped
    """

    return stop_with_goodbye() if (answer := input(question)) == "quit" else answer


if __name__ == "__main__":
    while True:
        quit_confirmation(
            "This is a trial, type anything, the program will stop if you type 'quit': "
        )
