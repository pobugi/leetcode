from typing import List

s = ["h", "e", "l", "l", "o"]


def solve(s: List[str]):
    c = len(s) - 1
    for i in range(c, -1, -1):
        s.append(s[i])
        s.pop(i)

    return s


print(solve(s))
