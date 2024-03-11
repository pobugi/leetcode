order = "cba"
s = "abcd"

# Output:  "cbad"


class Solution:
    def customSortString(self, s: str, order: str) -> str:
        result = ""
        s_dict = dict()
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        for letter in order:
            while s_dict.get(letter, 0) > 0:
                result += letter
                s_dict[letter] -= 1
        for letter in s_dict:
            qty = s_dict[letter]
            if qty > 0:
                result += letter * qty

        return result


print(Solution().customSortString(s, order))
