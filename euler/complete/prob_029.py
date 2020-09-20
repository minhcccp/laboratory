# From: https://projecteuler.net/problem=29

if __name__ == "__main__":
    print(len({base ** power for base in range(2, 101) for power in range(2, 101)}))
