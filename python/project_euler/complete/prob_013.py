# From: https://projecteuler.net/problem=13

if __name__ == "__main__":
    print(str(sum(int(number) for number in open("p013_numbers.txt").readlines()))[:10])
