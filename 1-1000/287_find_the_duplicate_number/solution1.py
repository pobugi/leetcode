from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = set()
        for num in nums:
            if num in hash:
                return num
            hash.add(num)
        return None

    def findDuplicateBinary(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            end = len(nums) - 1
            find = self.binary_search(nums, target, start=i + 1, end=end)
            if find != -1:
                return target
        return -1

    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            m = nums[mid]
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


s = Solution()
nums = [1, 3, 4, 2, 2]
print(s.findDuplicate(nums))
print(s.findDuplicateBinary(nums))
