strs = ["flower", "flow", "flight"]


def solve(strs: list):
    if not strs:
        return None
    if len(strs) == 1:
        return strs[0]
    max_prefix = strs[0]
    for word in strs[1:]:
        max_prefix = compare(max_prefix, word)
    return max_prefix


def compare(s1: str, s2: str) -> str:
    i = 0
    j = 0
    while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
        i += 1
        j += 1
    return s1[:i]


print(solve(strs))
