class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            if not words[i]:
                return False
            if words[i][0] != s[i]:
                return False
        return True


s = Solution()
assert s.isAcronym(words=["alice", "bob", "charlie"], s="abc") is True
assert s.isAcronym(words=["an", "apple"], s="a") is False
assert s.isAcronym(words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy") is True
