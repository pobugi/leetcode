n = 8


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [i for i in range(1, n + 1)]
        left = nums[0]
        right = sum(nums)
        for i in range(1, len(nums)):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i - 1]
        return -1


print(Solution().pivotInteger(n))
