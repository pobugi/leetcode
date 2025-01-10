class Solution:
	def scoreOfString(self, s: str) -> int:
		if len(s) <= 1:
			return 0
		result = 0
		for i in range(len(s) - 1):
			diff = abs(ord(s[i]) - ord(s[i + 1]))
			result += diff
		return diff


s = Solution()
print(s.scoreOfString("hello"))