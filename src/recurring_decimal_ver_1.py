"""
Resource(s):
https://en.wikipedia.org/wiki/Repeating_decimal

"""

from sympy import primefactors, divisors


def reptend_length(denominator: int) -> int:
    """
    :param denominator: Denominator of the fraction to be converted into decimal representation
    :return: Length of the reptend (infinitely repeated digit sequence) in the representation
    """

    if abs(denominator) < 2:
        raise ValueError("The modulus of the denominator must be greater than 1")

    try:
        value: int
        max_prime_factor: int
        prime_factor: int
        for value in divisors(
            (max_prime_factor := max(set(primefactors(denominator)).difference({2, 5})))
            - 1
        ):
            if 10 ** value % max_prime_factor == 1:
                return value

    except IndexError:
        return 0


if __name__ == "__main__":
    for number in range(2, 50):
        print(number, reptend_length(number))

    print(reptend_length(67))
