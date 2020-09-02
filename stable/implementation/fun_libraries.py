from datetime import datetime
from decimal import Decimal
from random import choice
from re import match

from matplotlib import pyplot

if __name__ == "__main__":
    pyplot.plot(range(1, 13), [choice(range(1000)) for time in range(12)])
    pyplot.show()

    print(Decimal("0.2") + Decimal("0.69"))
    print(Decimal("0.53") * Decimal("0.65"))

    birth = datetime(2002, 2, 8)  # Friday
    print(birth.day, birth.weekday())
    print(datetime.now(), datetime.now() - birth)
    # More info on datetime library: https://youtu.be/smDBZDvsm0I

    print(["OUT", "IN"][bool(match("^a...s$", "abyss"))])
