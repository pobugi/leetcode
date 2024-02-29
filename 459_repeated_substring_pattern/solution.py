class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            substr = s[:i]
            if len(s) % len(substr):
                continue
            mult = len(s) // len(substr)

            attempt = substr * mult
            if attempt == s:
                return True
        return False


s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("bb"))
print(s.repeatedSubstringPattern("abaababaab"))
print(s.repeatedSubstringPattern("zzz"))
