# Given a function that generates a random float between 0 and 1, calculate Pi
from math import hypot, pi
from random import random


def pi_estimation(number_of_points: int) -> float:
    return (
        4
        / len(
            length_list := [
                hypot(*[random() for _ in range(2)]) for _ in range(number_of_points)
            ]
        )
        * sum(length <= 1 for length in length_list)
    )


if __name__ == "__main__":
    for trial in range(10):
        for order in range(2, 8):
            print(
                trial,
                order,
                (result := pi_estimation(10 ** order)),
                abs(result / pi - 1) * 100,
            )
