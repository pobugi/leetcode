word1 = "ab"
word2 = "pqrs"
# Output: "apbqrs"


def solution(word1, word2):
    i, j = 0, 0
    result = []

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        i += 1
        result.append(word2[j])
        j += 1
    if i < len(word1):
        result.append(word1[i:])
    else:
        result.append(word2[j:])

    return "".join(result)


print(solution(word1, word2))
