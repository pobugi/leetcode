from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 3:
            return "Pending"
        board = [[None for i in range(3)] for i in range(3)]
        # fill the board
        i = 0
        while i < len(moves):
            firstx, firsty = moves[i]
            board[firstx][firsty] = "A"
            i += 1
            if i >= len(moves):
                break
            secondx, secondy = moves[i]
            board[secondx][secondy] = "B"
            i += 1
        result = self.checkWinner(board)
        if result is not None:
            return result
        for row in board:
            if None in row:
                return "Pending"
        return "Draw"

    def checkWinner(self, moves):
        # row / col / diag

        for row in moves:
            row_set = set(row)
            if len(row_set) == 1 and row_set != {None}:
                return row_set.pop()
        for i in range(len(moves)):
            col = [moves[j][i] for j in range(len(moves[i]))]
            col_set = set(col)
            if len(col_set) == 1 and col_set != {None}:
                return col_set.pop()
        # diag
        diag1 = [moves[0][0], moves[1][1], moves[2][2]]
        diag1_set = set(diag1)
        if len(diag1_set) == 1 and diag1_set != {None}:
            return diag1_set.pop()

        diag2 = [moves[0][2], moves[1][1], moves[2][0]]
        diag2_set = set(diag2)
        if len(diag2_set) == 1 and diag2_set != {None}:
            return diag2_set.pop()

        return None


s = Solution()
print(s.tictactoe([[0, 2], [0, 1], [2, 1]]))
