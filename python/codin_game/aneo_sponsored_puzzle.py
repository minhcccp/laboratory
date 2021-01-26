# region
"""\
GOAL

You enter a section of road, and you plan to rest entirely on your cruise control to cross the area without having to
stop or slow down.

The goal is to find the maximum speed (off speeding) that will allow you to cross all the traffic lights to green.

Warning: You can not cross a traffic light the second it turns red!

Your vehicle enters the zone directly at the speed programmed on the cruise control which ensures that it does not
change anymore.

INPUT

Line 1: An integer speed for the maximum speed allowed on the portion of the road (in km/h).

Line 2: An integer lightCount for the number of traffic lights on the road.

lightCount next lines:

- An integer distance representing the distance of the traffic light from the starting point (in meters).

- An integer duration representing the duration of the traffic light on each color.

A traffic light alternates a period of duration seconds in green and then duration seconds in red.

All traffic lights turn green at the same time as you enter the area.

OUTPUT

Line 1: The integer speed (km/h) as high as possible that cross all the green lights without committing speeding.
"""
# endregion

from typing import Annotated

if __name__ == "__main__":
    max_velocity: Annotated[int, "km/h"] = int(input())

    print(
        max(
            set.intersection(
                *[
                    {
                        speed
                        for speed in range(1, max_velocity + 1)
                        if not (distance * 3.6) // (speed * period) % 2
                    }
                    for distance, period in dict(
                        map(int, input().split()) for _ in range(int(input()))
                    ).items()
                ]
            )
        )
    )
