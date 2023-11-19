str1 = "ABAABAABA"
str2 = "ABAABA"


def solve(str1: str, str2: str):
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    substr = str2
    while substr:
        count1 = len(str1) // len(substr)
        count2 = len(str2) // len(substr)
        if len(str2) % len(substr) or len(str1) % len(substr):
            substr = substr[:-1]
            continue
        if count1 * substr == str1 and count2 * substr == str2:
            return substr
        substr = substr[:-1]
    return ""


print(solve(str1, str2))
