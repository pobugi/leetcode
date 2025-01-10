# 1 - true
# 16 - true
# 3 - false

def power_of_two_binary(n):
    rng = range(1, n // 2 + 1)

    start = 0
    end = len(rng)

    while start <= end:
        mid = (start + end) // 2

        curr = 2 ** mid

        if curr == n:
            return True
        if curr < n:
            start = mid + 1
        else:
            end = mid - 1

    return False


def power_of_two_divide(n):
    if n <= 0:
        return True
    while n > 1:
        if n % 2:
            return False
        n /= 2
    return True


print(power_of_two_divide(2147483646))
