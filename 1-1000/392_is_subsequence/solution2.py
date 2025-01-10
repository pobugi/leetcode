"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


def solve(s: str, t: str) -> bool:
    desired_len = len(s)
    j = 0

    for letter in s:
        while j < len(t):
            if t[j] == letter:
                desired_len -= 1
                j += 1
                break
            j += 1
    return desired_len == 0


print(solve(s="abc", t="ahbgdc"))
