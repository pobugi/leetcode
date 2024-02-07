def solution(words, x):
    result = []
    for i in range(len(words)):
        if x in words[i]:
            result.append(i)
    return result


print(solution(words=["leet", "code"], x="e"))  # [0,1]
print(solution(words=["abc", "bcd", "aaaa", "cbc"], x="a"))  # [0,2]
print(solution(words=["abc", "bcd", "aaaa", "cbc"], x="z"))  # []
