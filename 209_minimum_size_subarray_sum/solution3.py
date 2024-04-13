target = 7
nums = [2, 3, 1, 2, 4, 3]


def solve(nums: list[int], target: int):
    left = 0
    right = 0
    total = 0
    min_len = float("inf")

    while right < len(nums) and left < len(nums):
        while total < target:
            total += nums[right]
            right += 1
        while total >= target:
            min_len = min(right - left, min_len)
            total -= nums[left]
            left += 1
    return min_len


print(solve(nums, target))
