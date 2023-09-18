def solve(nums: list, target: int):

    i = 0
    j = 0

    curr_sum = nums[i]
    result = []
    while i < len(nums) and j < len(nums):
        while j < len(nums) - 1 and curr_sum < target:
            j += 1
            curr_sum += nums[j]

        if curr_sum >= target:
            result.append(j - i + 1)

        curr_sum -= nums[i]
        i += 1
    return min(result)


print(solve([2, 3, 1, 2, 4, 3], 7))
# print(solve([1, 1, 1, 1], 7))
