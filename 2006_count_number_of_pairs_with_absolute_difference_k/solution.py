def solve_wrong(nums: list[int], k: int):
    result = 0
    hash = {value: index for index, value in enumerate(nums)}
    print(hash)
    for i, num in enumerate(nums):
        target1, target2 = (abs(nums[i] - 2), abs(nums[i] + 2))
        if target1 in hash and hash[target1] > i:
            result += 1
        if target2 in hash and hash[target2] > i:
            result += 1

    return result


def solve(nums: list[int], k: int):
    result = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                result += 1
    return result


print(solve(nums=[3, 2, 1, 5, 4], k=2))
print(solve(nums=[1, 2, 2, 1], k=1))
