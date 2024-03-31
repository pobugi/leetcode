from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        vowels_dict = defaultdict(int)
        for letter in s:
            if letter in vowels:
                vowels_dict[letter] += 1

        for i in range(len(s)):
            if s[i] in vowels:
                for vowel in vowels:
                    if vowels_dict[vowel] > 0:
                        replacement = vowel
                        vowels_dict[replacement] -= 1
                        s = s[:i] + replacement + s[i + 1 :]
                        break
        return s


print(Solution().sortVowels("lEetcOde"))
