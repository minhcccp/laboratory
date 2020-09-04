# From: https://projecteuler.net/problem=1

if __name__ == "__main__":

    def div_number_sum(upper_bound: int, divisor: int) -> int:
        return (
            divisor * (scaled_bound := upper_bound // divisor) * (scaled_bound + 1) // 2
        )

    print(
        div_number_sum((target := 999), 3)
        + div_number_sum(target, 5)
        - div_number_sum(target, 15)
    )
