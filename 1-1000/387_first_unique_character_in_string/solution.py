s = "loveleetcode"


def solution(s):
    hash_table = dict()
    for letter in s:
        hash_table[letter] = 1 + hash_table.get(letter, 0)
    for i in range(len(s)):
        if hash_table[s[i]] == 1:
            return i
    return -1


print(solution(s))
