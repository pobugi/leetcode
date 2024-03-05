def solve(s: str) -> int:
    start = 0
    end = len(s) - 1

    while start <= end:
        if start > end:
            return 0
        if start == end:
            return 1

        if s[start] != s[end]:
            return end - start + 1

        curr = s[start]
        while s[start] == curr:
            start += 1
            if start > end:
                return 0
        while s[end] == curr:
            end -= 1
            if start > end:
                return 0

    return end - start + 1 if end > start else 0


print(solve(s="aabccabba"))
print(solve(s="cabaxfabac"))
print(solve(s="bbbbbbbbbbbbbbbbbbb"))
print(solve(s="bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
print(
    solve(
        s="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbacccabbabccaccbacaaccacacccaccbbbacaabbccbbcbcbcacacccccccbcbbabccaacaabacbbaccccbabbcbccccaccacaccbcbbcbcccabaaaabbbbbbbbbbbbbbb"
    )
)
