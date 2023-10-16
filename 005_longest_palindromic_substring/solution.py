class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            s1 = self.expand_from_middle(s, i, i)
            s2 = self.expand_from_middle(s, i, i + 1)
            sx = s1 if len(s1) > len(s2) else s2
            result = sx if len(sx) > len(result) else result

        return result

    def expand_from_middle(self, s, left, right):
        max_len_substr = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            substr = s[left : right + 1]
            if len(substr) > len(max_len_substr):
                max_len_substr = substr
            left -= 1
            right += 1
        return max_len_substr


s = Solution()
print(s.longestPalindrome("babad"))
