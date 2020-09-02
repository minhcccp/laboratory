# From: https://projecteuler.net/problem=89
from roman_numeral import roman_encoder, roman_decoder

if __name__ == "__main__":
    print(
        sum(
            len(stripped_entry) - len(roman_encoder(roman_decoder(stripped_entry)))
            for stripped_entry in [entry.strip() for entry in open("p089_roman.txt")]
        )
    )
