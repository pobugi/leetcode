from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        result = []
        for i, j in zip(l, r):
            result.append(self.is_arithmetic(nums[i : j + 1]))
        return result

    def is_arithmetic(self, arr: list[int]):
        if len(arr) < 3:
            return True
        arr.sort()
        delta = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != delta:
                return False
        return True


s = Solution()
print(s.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
print(
    s.checkArithmeticSubarrays(
        nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
        l=[0, 1, 6, 4, 8, 7],
        r=[4, 4, 9, 7, 9, 10],
    )
)
