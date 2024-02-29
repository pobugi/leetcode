from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        increasing = True
        decreasing = True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # increasing
                continue
            else:
                increasing = False
        if increasing:
            return True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:  # decreasing
                continue
            else:
                decreasing = False
        if decreasing:
            return True
        return False


s = Solution()
print(s.isMonotonic([3, 4, 2, 3]))
print(s.isMonotonic([3, 4, 4, 9]))
