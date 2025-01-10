nums = [1, 2, 3, 1, 2, 3]
k = 2  # true


def solve(nums: list, k: int):
    hash_map = {}  # value: indexes

    for i in range(len(nums)):
        value = nums[i]
        if value in hash_map:
            hash_map[value].append(i)
        else:
            hash_map[value] = [i]

    for key in hash_map:
        if len(hash_map[key]) > 1:
            for i in range(1, len(hash_map[key])):
                if abs(hash_map[key][i] - hash_map[key][i - 1]) <= k:
                    return True
    return False


print(solve(nums, k))
