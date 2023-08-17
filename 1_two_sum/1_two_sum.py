# https://leetcode.com/problems/two-sum/

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""


def solve(nums, target):
    cache = {}

    for i in range(len(nums)):
        value_needed = target - nums[i]
        if value_needed in cache:
            return [cache[value_needed], i]
        cache[nums[i]] = i
    return None


assert solve(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert solve(nums=[3, 2, 4], target=6) == [1, 2]
assert solve(nums=[3, 3], target=6) == [0, 1]
assert solve(nums=[3, 6], target=6) == None

print("task solved!")
