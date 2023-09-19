s = "anagram"
t = "nagaram"


def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    lst1 = list(s)
    lst2 = list(t)
    lst1.sort()
    lst2.sort()

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


print(solve(s, t))
