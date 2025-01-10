arr = [1, 2, 2, 1, 1, 3]


def solve(arr):
    data = {}

    for item in arr:
        data[item] = 1 + data.get(item, 0)
    return len(data.values()) == len(set(data.values()))


print(solve(arr))
