class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i - 1] == nums[i]:
                nums.pop(i - 1)
            i += 1
        return len(nums)
