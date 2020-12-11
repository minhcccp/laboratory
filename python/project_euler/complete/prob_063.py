# From: https://projecteuler.net/problem=63

if __name__ == "__main__":
    total: int = 0
    for number in range(1, 10):
        power: int = 1
        while power <= (exponential_length := len(str(number ** power))):
            if power == exponential_length:
                total += 1

            power += 1

    print(total)
