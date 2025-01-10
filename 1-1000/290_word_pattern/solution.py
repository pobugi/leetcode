"""
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


def solve(pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern) != len(words):
        return False
    word_to_char = {}
    char_to_word = {}
    for char, word in zip(pattern, words):
        if char in char_to_word and word != char_to_word[char]:
            return False
        if word in word_to_char and char != word_to_char[word]:
            return False
        char_to_word[char] = word
        word_to_char[word] = char

    return True


print(solve(pattern="abba", s="dog cat cat dog"))  # True
print(solve(pattern="abba", s="dog cat cat fish"))  # False
print(solve(pattern="aaaa", s="dog cat cat dog"))  # False
print(solve(pattern="abba", s="dog dog dog dog"))  # False
