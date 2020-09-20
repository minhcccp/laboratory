# From: https://en.wikipedia.org/wiki/Fizz_buzz
from typing import Dict

from numpy import long
from sympy.ntheory import primefactors

from scripts_with_inputs import quit_confirmation

if __name__ == "__main__":
    max_value: long = 0
    while max_value < 1:
        try:
            max_value = long(quit_confirmation("How much: "))
        except ValueError:
            continue

    reference: Dict[long, str] = {3: "Fizz", 5: "Buzz"}
    print(
        "\n".join(
            "".join(reference.get(prime, "") for prime in primefactors(num)) or str(num)
            for num in range(1, max_value + 1)
        )
    )