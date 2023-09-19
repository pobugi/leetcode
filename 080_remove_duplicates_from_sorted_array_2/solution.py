from typing import List


def solve(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    i = 2

    while i < len(nums):
        if nums[i] == nums[i - 1] == nums[i - 2]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


print(solve([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solve([5, 5]))
