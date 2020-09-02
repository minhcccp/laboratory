from sys import exit
from time import sleep
from typing import Union, Any

from numpy import long
from sympy import Integer

# Set up the directory of the package
__all__ = [
    "FULL_INTEGER_CLASS",
    "is_integer",
    "QUIT_REMINDER",
    "quit_confirmation",
    "palindrome_checker",
]

# Define the integer class including both the default int and the int class from numpy and sympy, along with a
# checking func
FULL_INTEGER_CLASS = Union[int, long, Integer]


def is_integer(checking_object: Any) -> bool:
    """
    :param checking_object: Object to be checked
    :return: Boolean value whether object is an integer
    """

    return isinstance(checking_object, FULL_INTEGER_CLASS.__args__)


if __name__ == "__main__":
    print(is_integer(3))
    print(is_integer(long(1e100)))
    print(is_integer(3.0))

# Define the features for interacting scripts/modules
QUIT_REMINDER: str = "Type 'quit' at any time to stop the program"


def quit_confirmation(question: str = "") -> str:
    """
    :param question: The prompt itself
    :return: Answer for the prompt, except the program will stop if the answer is "quit"
    """

    if (answer := input(question)) == "quit":
        print("Thanks for using the program, see ya! From MinhCCCP")
        sleep(10)
        exit()

    return answer


if __name__ == "__main__":
    while True:
        quit_confirmation(
            "This is a trial, type anything, the program will stop if you type 'quit': "
        )
