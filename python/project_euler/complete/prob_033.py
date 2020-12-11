from fractions import Fraction as Fra
from math import prod

if __name__ == "__main__":
    possible_set: set[int] = set(range(11, 100)) - set(range(20, 100, 10))
    result_list: list[Fra] = []

    den: int
    for den in possible_set:

        num: int
        for num in possible_set:
            if num == den:
                break

            chosen: Fra
            if num % 10 == den // 10 and (chosen := Fra(num, den)) == Fra(
                num // 10, den % 10
            ):
                result_list.append(chosen)

    print(prod(result_list))
