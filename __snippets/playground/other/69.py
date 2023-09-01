def sqrt(x):
    if x in (0, 1):
        return x
    start = 1
    end = x

    while start <= end:

        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid > x:
            end = mid
        else:
            start = mid
    return None



print(sqrt(8))