# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"


def solve(s: str, part: str):
    i = 0
    while i < len(s) - len(part) + 1:
        while i < len(s) - len(part) + 1 and s[i : i + len(part)] == part:
            s = s[:i] + s[i + len(part) :]
            i -= len(part)
            i = max(i, 0)
        i += 1
    return s


print(solve(s="daabcbaabcbc", part="abc"))
