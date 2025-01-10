from typing import List

# Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: 25


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j or i + j == len(mat) - 1:
                    result += mat[i][j]
        return result


s = Solution()
print(s.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
