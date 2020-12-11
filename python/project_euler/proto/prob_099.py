from bidict import bidict

if __name__ == "__main__":
    couple_bidict: bidict[int, int] = bidict()

    input_list: list[list[int]]
    number: str
    line: str
    couple_bidict.forceupdate(
        sorted(
            input_list := [
                [int(number) for number in line.split(",")]
                for line in open("prob_099.txt")
            ]
        )
    )

    print(list(couple_bidict.items())[:10])
