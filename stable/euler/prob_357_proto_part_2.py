from numpy import long

if __name__ == "__main__":
    total: long = 0
    for num in open("prob_357_proto.txt").readlines():
        total += int(num)
        print(total)
