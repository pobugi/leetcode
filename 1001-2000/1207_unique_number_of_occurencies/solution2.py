arr = [1, 2, 2, 1, 1, 3]


def solve(arr):
    data = dict()
    unique_occurencies = set()

    for item in arr:
        data[item] = 1 + data.get(item, 0)
    for item in data.values():
        if item in unique_occurencies:
            return False
        unique_occurencies.add(item)
    return True


print(solve(arr))
