class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict, t_dict = dict(), dict()
        for index, letter in enumerate(s):
            s_dict[letter] = index
        for index, letter in enumerate(t):
            t_dict[letter] = index
        result = 0

        for letter in s_dict:
            result += abs(s_dict[letter] - t_dict[letter])
        return result


s = Solution()
print(s.findPermutationDifference("abcde", "edbac"))
