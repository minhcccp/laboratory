# From: https://projecteuler.net/problem=89
from roman_numeral import encoder, decoder

if __name__ == "__main__":
    with open("p089_roman.txt") as roman_numerals:
        print(
            sum(
                len(stripped_entry := entry.strip())
                - len(encoder(decoder(stripped_entry)))
                for entry in roman_numerals
            )
        )
