"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

data = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def combinations(lst1, lst2):
    res = []
    for letter1 in lst1:
        for letter2 in lst2:
            res.append(f"{letter1}{letter2}")
    return res


def solve(digits):
    if not digits:
        return ""
    if len(digits) == 1:
        return data[digits]
    if len(digits) == 2:
        return combinations(data[digits[0]], data[digits[1]])
    if len(digits) == 3:
        return combinations(combinations(data[digits[0]], data[digits[1]]), data[digits[2]])
    if len(digits) == 4:
        return combinations(
            combinations(combinations(data[digits[0]], data[digits[1]]), data[digits[2]]), data[digits[3]]
        )
