arr = [1, 0, 0, 1, 2, 2, 55, 0]


def solve(arr):

    n = len(arr)
    i = 0

    while i < n:

        if arr[i] == 0:
            arr.append(arr.pop(i))
            n -= 1
        else:
            i += 1
    return arr


print(solve(arr))
