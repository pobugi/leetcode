n = 16


def solve(n):

    if n < 0:
        return False
    if n in (0, 1):
        return True

    start = 1
    end = n

    while start <= end:
        mid = (end + start) // 2
        if mid * mid == n:
            return True
        if mid * mid > n:
            end = mid - 1
        else:
            start = mid + 1
    return False

print(solve(25))