from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        i = 0
        j = 0
        res = 0
        max_res = 0
        while i < len(nums) and j < len(nums):
            curr = nums[i]
            count[curr] += 1
            res += 1
            while count[curr] > k:
                curr2 = nums[j]
                count[curr2] -= 1
                j += 1
                res -= 1
            i += 1
            max_res = max(max_res, res)

        return max_res


s = Solution()
print(s.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2, 3], k=2))  # 6
print(s.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2, 3], k=3))  # 9
