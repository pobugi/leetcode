arr = [-1, 0, 1, 2, -1, -4]

def two_sum(arr, target):
    cache = dict()
    # result = []
    for i in range(len(arr)):
        value_needed = target - arr[i]
        if value_needed in cache:
            # result.append([i, cache[value_needed]])
            return [arr[i], value_needed]
        else:
            cache[arr[i]] = i
    # return result


for i in range(len(arr)):
    # print(arr[i])
    # print(arr[:i] + arr[i+1:])
    target = arr[i]
    arr2 = arr[:i] + arr[i+1:]
    two = two_sum(arr2, -target)
    if two:
        two.append(target)
        print(two)


