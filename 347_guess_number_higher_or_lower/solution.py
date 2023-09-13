from random import randint

i = 10000000000
n = randint(1, i)

print(f"Num to find: {n}")


def guess(num: int) -> int:
    if num == n:
        print("YEAH!")
        return 0
    if num < n:
        return 1
    else:
        return -1


def guess_number(n):
    start = 0
    end = n + 1

    while start <= end:
        mid = (start + end) // 2
        if guess(mid) == 0:
            return mid
        if guess(mid) == -1:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(guess_number(n))
