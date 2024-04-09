from typing import List

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != 0:
                    if row in rows:
                        matrix[row][col] = 0
                    if col in cols:
                        matrix[row][col] = 0


Solution().setZeroes(matrix)
for row in matrix:
    print(row)
