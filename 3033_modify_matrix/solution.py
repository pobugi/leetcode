from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        maxes = []
        for i in range(len(matrix[0])):
            maxes.append(max(matrix[j][i] for j in range(len(matrix))))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == -1:
                    matrix[i][j] = maxes[j]
        return matrix
