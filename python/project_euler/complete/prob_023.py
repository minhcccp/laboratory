from sympy.ntheory.factor_ import is_abundant as isa

if __name__ == "__main__":
    upper: int = 28_124
    start_set: set[int] = {number for number in range(12, upper - 12) if isa(number)}
    possible_numbers: set[int] = set()

    first_number: int
    for first_number in start_set:

        second_number: int
        for second_number in start_set:

            new_sum: int
            if (new_sum := first_number + second_number) < upper:
                possible_numbers.add(new_sum)
            else:
                break

    print(sum(set(range(upper)) - possible_numbers))
