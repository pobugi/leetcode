class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(nums: list[int], target: int, start: int, end: int) -> int:
            if not nums or start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binary_search(nums, target, start, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, end)

        return binary_search(nums, target, 0, len(nums) - 1)


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))  # 4
