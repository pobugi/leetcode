def solve(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        while left < len(s) and right < len(s) and not s[left].lower().isalnum():
            left += 1
        while left < len(s) and right < len(s) and not s[right].lower().isalnum():
            right -= 1

        if left < right and s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True


print(solve(s="A man, a plan, a canal: Panama"))
