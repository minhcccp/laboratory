# From: https://projecteuler.net/problem=30
from digital_function import pdi_function

if __name__ == "__main__":
    print(
        sum(
            number
            for number in range(10, int(1e6))
            if number == pdi_function(number, 5)
        )
    )
