"""
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Input: nums = [1,1,2]
Output: [1]

Input: nums = [1]
Output: []
"""


class Solution:
    def binary_search(self, nums: list[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def solve(self, nums: list[int]) -> list[int]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            target = nums[i]

            search_result = self.binary_search(nums, target, i + 1, len(nums) - 1)
            if search_result != -1:
                result.append(target)
        return result


s = Solution()
print(s.solve([4, 3, 2, 7, 8, 2, 3, 1]))
