# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def solve(nums: list, k: int):
    curr_sum = max_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        max_sum = max(curr_sum, max_sum)
    return max_sum


print(solve(nums=[1, 12, -5, -6, 50, 3], k=4))
