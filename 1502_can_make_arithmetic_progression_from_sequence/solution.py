from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr or len(arr) <= 2:
            return True

        arr.sort()
        step = arr[1] - arr[0]

        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) != step:
                return False
        return True


s = Solution()
print(s.canMakeArithmeticProgression([-68, -96, -12, -40, 16]))
