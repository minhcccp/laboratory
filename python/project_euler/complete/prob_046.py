from sympy import integer_nthroot, isprime

if __name__ == "__main__":
    current: int = 9

    while current < 1e4:
        biggest_candidate: int
        square_exist: bool
        biggest_candidate, square_exist = integer_nthroot((current - 3) // 2, 2)

        if not square_exist:
            square_exist = any(
                isprime(current - 2 * square_candidate ** 2)
                for square_candidate in range(1, biggest_candidate + 1)
            )

        print(current, square_exist)

        if not square_exist:
            break

        while isprime(current := current + 2):
            continue
