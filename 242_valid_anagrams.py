# https://leetcode.com/problems/valid-anagram/


def fill_dict(s: str) -> dict:
    res = {}

    for letter in s:
        if letter in res:
            res[letter] += 1
        else:
            res[letter] = 1
    return res


def valid_anagram(s: str, t: str) -> bool:
    return fill_dict(s) == fill_dict(t)


assert valid_anagram("anagram", "nagaram") is True
assert valid_anagram("rat", "car") is False
print("success")
