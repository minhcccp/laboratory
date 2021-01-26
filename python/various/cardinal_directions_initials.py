"""
Given a string of cardinal directions' initials, return
- The simplified number of steps to be taken
- The angle of the destination to the reference direction (i.e. East)
"""
from cmath import phase
from math import degrees

if __name__ == "__main__":
    print(
        int(
            abs(
                vertical := (
                    solution := sum(
                        {"N": 1j, "S": -1j, "E": 1, "W": -1}[letter]
                        for letter in input().upper()
                    )
                ).imag
            )
        ),
        ["N", "S"][vertical < 0],
        " ",
        int(abs(horizontal := solution.real)),
        ["E", "W"][horizontal < 0],
        "\n",
        f"Angle: {round(radians := phase(solution), ndigits=2)} radians / {round(degrees(radians), ndigits=2)} degrees",
        sep="",
    )
