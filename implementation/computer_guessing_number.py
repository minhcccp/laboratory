from scripts_with_inputs import QUIT_REMINDER, quit_confirmation, stop_with_goodbye

if __name__ == "__main__":
    print(QUIT_REMINDER)

    number_of_digits: int = 0
    while number_of_digits < 1:
        try:
            number_of_digits = int(quit_confirmation("How many digit does your number have: "))
        except ValueError:
            continue

    current: int = 10 ** number_of_digits // 2
    difference: int = current
    number: int = 1

    while True:
        try:
            print(f"The computer guesses your number is {current}")

            option = int(
                input(
                    "Type 0 if the guess is correct, -1 if higher than your number or 1 if lower: "
                )
            )
            if option in range(-1, 2):
                if option == 0:
                    print(f"Hooray! The computer has guessed {number} time(s)")
                    stop_with_goodbye()

                current += option * difference
                if difference > 1:
                    difference //= 2

                number += 1

        except ValueError:
            continue
