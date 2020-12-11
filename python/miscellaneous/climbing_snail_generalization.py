"""
Given:
- The total distance d
- The forward distance per unit time f
- The backward distance per unit time b
Find the time it takes to complete the given distance, or print "Impossible"
"""
from math import ceil

if __name__ == "__main__":

    def time_finder(distance: float, forward: float, backward: float) -> int:
        if forward >= distance:
            return 1

        if backward >= forward:
            return 0

        return ceil((distance - backward) / (forward - backward))

    if (
        time := time_finder(
            *(float(number) for number in input("Type the value for d, f, b: ").split())
        )
    ) :
        print(time)

    else:
        print("Impossible")
