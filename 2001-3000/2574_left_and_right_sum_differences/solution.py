class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left, last = [0], 0
        for i in range(len(nums) - 1):
            curr = last + nums[i]
            left.append(curr)
            last = curr

        right, last = [0], 0
        for i in range(len(nums) - 1, 0, -1):
            curr = last + nums[i]
            right = [curr] + right
            last = curr

        return [abs(l - r) for l, r in zip(left, right)]
