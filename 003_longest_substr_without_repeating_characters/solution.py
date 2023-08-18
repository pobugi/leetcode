# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

s = "abcabcd"


def solve(s):
    i = 0
    j = 0
    max_len = 0

    lst = set()

    while i < len(s) and j < len(s):
        while j < len(s):
            if not s[j] in lst:
                lst.add(s[j])
                j += 1
            else:
                i += 1
                j = i
                break
        max_len = max(len(lst), max_len)
        lst = set()

    return max_len

print(solve(s))
