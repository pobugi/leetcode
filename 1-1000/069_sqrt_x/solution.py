def solve(x):
    left, right = 0, x

    while left <= right:
        mid = (right + left) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid + 1
            res = mid
        else:
            right = mid - 1
    return res


print(solve(14))
