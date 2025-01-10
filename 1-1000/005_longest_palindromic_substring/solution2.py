s = "bkabakb"


def expand_from_middle(s: str):
    i = 0
    max_len = 0
    result = ""
    while i < len(s):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # print(f"{s[left : right + 1]}, {right - left}")
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                result = s[left : right + 1]
            left -= 1
            right += 1
        i += 1

    i = 0

    while i < len(s):
        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # print(f"{s[left : right + 1]}, {right - left + 1}")
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                result = s[left : right + 1]

            left -= 1
            right += 1
        i += 1
    return result


print(expand_from_middle(s))
