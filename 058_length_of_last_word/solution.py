def solve(s: str) -> int:

    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalpha():
            while i > -1 and s[i].isalpha():
                i -= 1
                cnt += 1
            return cnt
    return cnt


print(solve("Hello World"))  # 5
print(solve("   fly me   to   the moon  "))  # 4
print(solve("luffy is still joyboy"))  # 6
print(solve("a"))  # 1
