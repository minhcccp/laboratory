# From: https://projecteuler.net/problem=19
from datetime import date

if __name__ == "__main__":
    print(
        sum(
            date(year, month, 1).weekday() == 6
            for year in range(1901, 2001)
            for month in range(1, 13)
        )
    )
