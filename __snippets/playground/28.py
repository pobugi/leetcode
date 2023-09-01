haystack = "sadbutsad"
needle = "sad"


for i in range(len(haystack) - len(needle) + 1):
    substr = haystack[i: i + len(needle)]
    if substr == needle:
        print(i)


