from sys import exit
from time import sleep

QUIT_REMINDER: str = "Type 'quit' at any time to stop the program"


def quit_confirmation(question: str = "") -> str:
    """
    Check if the user wants to stop the program by answering "quit" in a prompt

    :param question: The prompt itself
    :return: The answer for the prompt if it's not "quit"
    """

    if not question or (answer := input(question)) == "quit":
        print("Thanks for using the program, see ya! From MinhCCCP")
        sleep(10)
        exit()

    return answer


if __name__ == "__main__":
    while True:
        quit_confirmation(
            "This is a trial, type anything, the program will stop if you type 'quit': "
        )
