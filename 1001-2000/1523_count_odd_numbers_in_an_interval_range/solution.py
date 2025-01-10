class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 or high % 2:
            return (high - low) // 2 + 1
        return (high - low) // 2


s = Solution()
print(s.countOdds(8, 10))
print(s.countOdds(8, 11))
