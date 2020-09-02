# From: https://projecteuler.net/problem=13
from numpy import long

if __name__ == "__main__":
    print(str(sum(long(number) for number in open("p013_numbers.txt").readlines()))[:10])
