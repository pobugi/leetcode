# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
from collections import defaultdict

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def validate(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)  # key: (row // 3, col // 3)

    for row in range(9):  # rows
        for col in range(9):  # cols
            if board[row][col] == ".":
                continue
            if (
                board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row // 3, col // 3)]
            ):
                return False
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])
    return True


print(validate(board))
