class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr_len = 0
        last_len = 0
        left = 0
        right = 0
        while right < len(s) and left < len(s):
            last_len = curr_len
            curr_len = 0
            while right < len(s) and s[right] == " ":
                right += 1
                left += 1
            while right < len(s) and s[right] != " ":
                curr_len += 1
                right += 1
            curr_len = right - left
            left = right
        return curr_len or last_len


s = Solution()
print(s.lengthOfLastWord("Hello World"))  # 5
print(s.lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(s.lengthOfLastWord("luffy is still joyboy"))  # 6
print(s.lengthOfLastWord("Today is a nice day"))  # 3
