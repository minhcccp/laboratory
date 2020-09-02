"""
You are given a row of N light bulbs, represented by a string of 0 or 1, totally N characters in the string.
0 means the light bulb is OFF.
1 means the light bulb is ON.

The left-most character is light bulb 1.
The right-most character is light bulb N.

Each light bulb has an independent switch allowing you to switch it ON or OFF.

To switch ON/OFF any light bulb, there are two rules:

Rule 1 - You can change the state of light bulb i if i+1 is ON AND i+2, i+3,... N are OFF.
Rule 2 - Rule 1 does not apply to light bulb N, which can be switched ON/OFF at will.

(
The rules if the order of the light bulbs is reversed:
1 - You can change the state of light bulb i if i-1 is ON AND i-2, i-3,..., up to and including 1 are OFF.
2 - The only exception is the first light bulb (light bulb 1), which can be switched ON/OFF at will.
)

The game starts with a given lighting pattern.
You will also have a target lighting pattern.

Find the minimum number of switches needed to change the pattern from start to target.

Example: To change pattern from 1101 to 0100:
1101 (start)
1100 (switch #4, by Rule 2)
0100 (switch #1, by Rule 1) - reached target by switching 2 times.
"""

if __name__ == "__main__":
    # start_state: str = input()
    # target_state: str = input()
    #
    # def main_task(inp_str: str) -> str:
    #     if inp_str == "0":
    #         return "1"
    #
    #     elif inp_str == "1":
    #         return "0"
    #
    # total_steps: int = 0
    #
    # if start_state[-1] != target_state[-1]:
    #     total_steps += 1
    #     start_state = start_state[:-1] + main_task(start_state[-1])

    reversed_start_list, reversed_target_list = [
        [bool(int(bulb)) for bulb in reversed(state)] for state in input().split()
    ]

    total_steps: int = 0

    if reversed_start_list[0] != reversed_target_list[0]:
        total_steps += 1
        reversed_start_list[0] = not reversed_start_list[0]

    while reversed_start_list != reversed_target_list:
        pass

    print(total_steps)
