s = "  hello world  "


def solve(s: str):
    words = s.split()
    result = []
    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])
    return " ".join(result)


print(solve(s))
