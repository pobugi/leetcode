# https://leetcode.com/problems/remove-element/

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


def solve(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return nums


print(solve(nums, val))
