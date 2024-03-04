from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negatives += 1
        return -1 if negatives % 2 else 1
