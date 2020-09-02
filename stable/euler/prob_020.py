# From: https://projecteuler.net/problem=20
from sympy import factorial

from digital_function import pdi_function

if __name__ == "__main__":
    print(pdi_function(int(factorial(100))))
