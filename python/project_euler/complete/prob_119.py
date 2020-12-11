def digital_sum(number: int) -> int:
    final: int = 0

    while number:
        final += number % 10
        number //= 10

    return final


if __name__ == "__main__":
    required = range(2, 69)

    record: list[int] = [
        candidate
        for base in required
        for power in required
        if digital_sum(candidate := base ** power) == base
    ]

    print(len(record), sorted(record)[29])
