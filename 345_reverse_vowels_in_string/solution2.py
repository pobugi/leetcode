class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        letters = [letter for letter in s if letter in vowels]
        if not letters:
            return s
        letters = letters[::-1]
        s_list = list(s)
        j = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = letters[j]
                j += 1
        return "".join(s_list)


s = Solution()
print(s.reverseVowels("LEETCODE"))
