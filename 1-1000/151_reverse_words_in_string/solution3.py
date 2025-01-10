class Solution:
	def reverseWords(self, s: str) -> str:
		i = 0
		result = []
		substr = ""
		while i < len(s):
			while i < len(s) and s[i] == ' ':
				i += 1
			while i < len(s) and s[i] != ' ':
				substr += s[i]
				i += 1
			result = [substr] + result if substr else result
			substr = ""
		return " ".join(result)

s = Solution()
print(s.reverseWords("the sky is blue"))  # "blue is sky the"
print(s.reverseWords("  hello world  "))  # "world hello"
print(s.reverseWords("a good   example"))  # "example good a"