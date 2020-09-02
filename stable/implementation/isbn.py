# From: https://en.wikipedia.org/wiki/International_Standard_Book_Number
def isbn_checker(isbn_string: str) -> bool:
    if (
        len(digits_list := [int(digit) for digit in isbn_string if digit.isdigit()])
        != 13
    ):
        raise ValueError("This program works with ISBN-13 only")

    return (
        not sum(
            3 * digit if index % 2 else digit for index, digit in enumerate(digits_list)
        )
        % 10
    )


if __name__ == "__main__":
    print(isbn_checker("978-0-306-40615-7"))
