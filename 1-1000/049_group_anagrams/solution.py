# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = {}

    for s in strs:
        letters = {letter: 0 for letter in ALPHABET}
        for letter in s:
            letters[letter] += 1
        key = tuple(letters.values())
        if key in result:
            result[key].append(s)
        else:
            result[key] = [s]

    return list(result.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
