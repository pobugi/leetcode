# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

haystack = "fsadbutsad"
needle = "sada"


def solve(haystack: str, needle: str) -> int:
    portion = len(needle)
    for i in range(len(haystack)):
        if needle == haystack[i: i + portion]:
            return i
    return - 1


print(solve(haystack, needle))
