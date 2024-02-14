# Input: nums = [3, 1, -2, -5, 2, -4]
# Output: [3, -2, 1, -5, 2, -4]


def solve(nums: list[int]):
    positive = []
    negative = []
    result = []
    for num in nums:
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)
    i = 0
    while i < len(positive) and i < len(negative):
        result.append(positive[i])
        result.append(negative[i])
        i += 1

    return result


print(solve([3, 1, -2, -5, 2, -4]))
