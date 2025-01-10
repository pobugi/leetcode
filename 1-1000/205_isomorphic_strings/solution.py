# s = "egg", t = "add" # true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping1 = dict()
        mapping2 = dict()

        for i in range(len(s)):
            first, second = s[i], t[i]
            if first in mapping1 and mapping1[first] != second:
                return False
            mapping1[first] = second
            if second in mapping2 and mapping2[second] != first:
                return False
            mapping2[second] = first

        return True

s = Solution()
# print(s.isIsomorphic("egg", "add"))
# print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("badc", "baba"))