def solve(s: str, t: str) -> bool:
    j = 0
    count = len(s)
    for i in range(len(s)):
        curr_letter = s[i]
        while j < len(t) and t[j] != curr_letter:
            j += 1
        if j < len(t) and t[j] == curr_letter:
            count -= 1
        j += 1
    return count == 0


print(solve("abc", "ahbgdc"))
print(solve("axc", "ahbgdc"))


def solve2(s: str, t: str) -> bool:
    j = 0
    counter = 0
    for letter in s:
        while j < len(t) and t[j] != letter:
            j += 1
        if j < len(t) and t[j] == letter:
            counter += 1
        j += 1
    return counter == len(s)


print(solve2("abc", "ahbgdc"))
print(solve2("axc", "ahbgdc"))
print(solve2(s="aaaaaa", t="bbaaaa"))
