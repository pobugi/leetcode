VOWELS = ["a", "e", "i", "o", "u"]


def solve(s: str, k: int):
    prev_slice = s[:k]
    curr_count = 0
    for letter in prev_slice:
        if letter in VOWELS:
            curr_count += 1
    max_count = curr_count
    prev_first = s[0]

    for i in range(1, len(s) - k + 1):
        curr_last = s[i + k - 1]
        if prev_first in VOWELS:
            curr_count -= 1
        if curr_last in VOWELS:
            curr_count += 1
        max_count = max(curr_count, max_count)
        prev_first = s[i]
    return max_count


s = "abciiidef"
k = 3

print(solve(s, k))
