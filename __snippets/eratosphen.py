def solve(n):
    arr = [i for i in range(2, n + 1)]

    i = 1

    while i < len(arr):
        print(arr[i:])
        i += 1

    # for i in range(len(arr)):
    #     for j in range(i * 2, len(arr)):
    #         if arr[j] % arr[i] == 0:
    #             arr.pop(j)

    return arr


print(solve(30))
