# From: https://projecteuler.net/problem=9
if __name__ == "__main__":
    for adjacent in range(3, 999):
        for opposite in range(adjacent + 1, 1000):
            if (
                hypotenuse := 1000 - adjacent - opposite
            ) ** 2 == adjacent ** 2 + opposite ** 2:
                print(hypotenuse * adjacent * opposite)
                exit()
