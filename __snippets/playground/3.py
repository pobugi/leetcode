def lengthOfLongestSubstring(s: str) -> int:
    i = 0
    j = 0
    max_len = 0

    lst = set()

    while i < len(s) and j < len(s):
        while j < len(s):
            if not s[j] in lst:
                print(s[i:j+1])
                lst.add(s[j])
                j += 1
            else:
                i += 1
                j = i
                break
        max_len = max(len(lst), max_len)
        lst = set()

    return max_len

print(lengthOfLongestSubstring("abcabcbb"))