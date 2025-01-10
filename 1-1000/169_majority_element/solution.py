"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


def solve(nums: list):
    nums.sort()
    mid_index = len(nums) // 2
    return nums[mid_index]


print(solve([3, 2, 3]))
print(solve([2, 2, 1, 1, 1, 2, 2]))
