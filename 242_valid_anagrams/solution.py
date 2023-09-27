s = "anagram"
t = "nagaram"


def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict1, dict2 = dict(), dict()

    for i in range(len(s)):
        dict1[s[i]] = 1 + dict1.get(s[i], 0)
        dict2[t[i]] = 1 + dict2.get(t[i], 0)
    for key in dict1:
        if dict1[key] != dict2.get(key):
            return False
    return True


print(solve(s, t))
