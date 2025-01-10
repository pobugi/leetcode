num = 133331


def solve(x):
    arr = []
    while x:
        arr.append(x % 10)
        x //= 10

    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


print(solve(num))
