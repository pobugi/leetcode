class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            num = self.decimal_to_base_number(n, base)
            if self.is_palindrome(num) is False:
                return False
        return True

    def decimal_to_base_number(self, decimal_number: int, base: int) -> list:
        result = []

        while decimal_number:
            remainder = decimal_number % base
            result.append(remainder)
            decimal_number = decimal_number // base
        return result[::-1]

    def is_palindrome(self, number: list):
        left, right = 0, len(number) - 1

        while left <= right:
            if number[left] != number[right]:
                return False
            left += 1
            right -= 1
        return True


s = Solution()
print(s.isStrictlyPalindromic(9))
print(s.isStrictlyPalindromic(4))
