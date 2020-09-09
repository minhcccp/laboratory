# Given a function that generates a random float between 0 and 1, calculate Pi
from math import hypot, pi
from random import random


def pi_estimation(number_of_points: int) -> float:
    return (
        4
        / len(
            points_list := [
                hypot(*[random() for coordinate in range(2)])
                for time in range(number_of_points)
            ]
        )
        * sum(point <= 1 for point in points_list)
    )


if __name__ == "__main__":
    for trial in range(10):
        for order in range(2, 9):
            print(
                trial,
                order,
                (result := pi_estimation(10 ** order)),
                abs(result / pi - 1) * 100,
            )
