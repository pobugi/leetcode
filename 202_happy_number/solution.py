class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = self.get_sum_of_squares(n)

        return False

    def get_sum_of_squares(self, n: int) -> int:
        result = 0
        while n:
            remainder = n % 10
            result += remainder * remainder
            n //= 10
        return result
