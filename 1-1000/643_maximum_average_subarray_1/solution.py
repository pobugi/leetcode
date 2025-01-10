# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


def solve(nums: list, k: int):
    first_subarr = nums[:k]
    curr_first = first_subarr[0]
    curr_sum = sum(first_subarr)
    max_sum = curr_sum

    for i in range(1, len(nums) - k + 1):
        curr_sum = curr_sum - curr_first + nums[i + k - 1]
        curr_first = nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k


print(solve(nums=[1, 12, -5, -6, 50, 3], k=4))
