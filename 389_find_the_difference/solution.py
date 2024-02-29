class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1, dict2 = dict(), dict()

        for letter in s:
            dict1[letter] = dict1.get(letter, 0) + 1
        for letter in t:
            dict2[letter] = dict2.get(letter, 0) + 1

        for letter in dict2:
            if letter not in dict1:
                return letter
            if dict2[letter] > dict1[letter]:
                return letter
        return ""


s = Solution()
print(s.findTheDifference("a", "aa"))
