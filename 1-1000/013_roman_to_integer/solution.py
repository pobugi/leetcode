class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1 and symbols[s[i + 1]] > symbols[s[i]]:
                res -= symbols[s[i]]
            else:
                res += symbols[s[i]]
        return res


s = Solution()
print(s.romanToInt("MCMXCIV"))
