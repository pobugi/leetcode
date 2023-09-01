s = "A man, a plan, a canal: Panama"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while right > left:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(valid_palindrome("0P"))

for letter in "abcdefghijklmnopqrstuvwxyz0123456789":
    print(ord(letter))