# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
from typing import List


def solution(words: List[str]) -> str | None:
    for word in words:
        if is_palindrome(word):
            return word
    return None


def is_palindrome(s: str) -> bool:
    if len(s) < 2:
        return True

    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
