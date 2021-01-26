from fractions import Fraction


def decompose(value: str) -> list:
    result: list = []
    initial_fraction: Fraction = Fraction(value)

    while initial_fraction:
        scaled_numerator: int = initial_fraction.numerator

        while (
            initial_fraction.denominator > 1
            and initial_fraction.denominator % scaled_numerator
        ):
            scaled_numerator -= 1

        unit_fraction: Fraction = Fraction(
            scaled_numerator, initial_fraction.denominator
        )

        initial_fraction -= unit_fraction
        result.append(str(unit_fraction))

    return result


if __name__ == "__main__":
    print(decompose("75/10"))
