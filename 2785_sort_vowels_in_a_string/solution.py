class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels_list = []

        for letter in s:
            if letter in vowels:
                vowels_list.append(letter)
        vowels_list.sort()
        for i in range(len(s)):
            if s[i] in vowels:
                vowel = vowels_list.pop(0)
                s = s[:i] + vowel + s[i + 1 :]
        return s
