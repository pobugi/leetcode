order = "cba"
s = "abcd"

# Output:  "cbad"


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        s_dict = dict()
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in order:
            if letter in s_dict and s_dict[letter] == 0:
                del s_dict[letter]
            while s_dict.get(letter, 0) > 0:
                result += letter
                s_dict[letter] -= 1

        for letter in s_dict:
            while s_dict[letter] > 0:
                result += letter
                s_dict[letter] -= 1

        return result


print(Solution().customSortString(order, s))
