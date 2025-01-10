def solve(s: str) -> int:
    i = 0  # pointer

    curr_len = 0
    while i < len(s):  # iterate through the string
        curr_len = 0  # current length of a word
        while i < len(s) and s[i] != " ":  # catch non-space characters and count its length
            curr_len += 1
            i += 1

        while i < len(s) and s[i] == " ":  # pass through all next space characters
            i += 1
    return curr_len  # return curr lentgth as it will be the length of the last word


print(solve("Hello World"))  # 5
print(solve("   fly me   to   the moon  "))  # 4
print(solve("luffy is still joyboy"))  # 6
print(solve("a"))  # 1
print(solve("a"))  # 1
print(solve("Today is a nice day"))  # 3
