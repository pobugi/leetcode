s = "abc"

t = "uyhahbgdc"

def solve(t, s):
    pass


def subseq(s, t):
    j = 0
    res = 0

    for i in range(len(s)):
        while j < len(t):
            if s[i] == t[j]:
                res += 1
                j += 1
                break
            j += 1
    return len(s) == res


print(subseq(s, t))