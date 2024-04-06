class Solution:
    def climbStairsWithHelper(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict):
        if not n in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def climb(n):
            if n not in memo:
                memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        climb(n)
        return memo[n]


s = Solution
