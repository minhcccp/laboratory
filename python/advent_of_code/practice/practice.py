from random import randint


def solution(xs):
    l = len(xs)
    if l == 1:
        return str(xs[0])

    final = 1
    count_zer = 0
    count_neg = 0
    max_neg = -1001
    for i in xs:
        if i:
            if i < 0:
                max_neg = max(max_neg, i)
                count_neg += 1

            final *= i

        else:
            count_zer += 1

    if count_zer == l:
        final = 0
    if count_neg:
        if count_neg == 1 and count_zer > 0 and count_neg + count_zer == l:
            final = 0
        else:
            final //= max_neg

    return str(final)


if __name__ == "__main__":
    print(solution([2, 0, 2, 2, 0]))
    print(solution([-2, -3, 4, -5]))
    print(solution([2, -3, 1, 0, -5]))
    eg = [randint(-1000, 1000) for _ in range(50)]
    print(eg)
    print(solution(eg))
