from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        curr = nums[0]

        while i < len(nums):
            if nums[i] == curr:
                nums.pop(i)
            else:
                curr = nums[i]
                i += 1
        return len(nums)
