from collections import defaultdict

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def solve(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)  # {(row, col): {}}

    for row in range(len(board)):
        for col in range(len(board[0])):
            curr = board[row][col]
            if curr == ".":
                continue
            if curr in rows[row]:
                print(f"row n: {row}, duplicate in row: {curr}")
                return False
            if curr in cols[col]:
                print(f"col n: {col}, duplicate in col: {curr}")
                return False

            squares_key = (row // 3, col // 3)
            if curr in squares[squares_key]:
                print(f"row n: {row}, col n: {col}, duplicate in square: {curr}")
                return False
            rows[row].add(curr)
            cols[col].add(curr)
            squares[squares_key].add(curr)
    return True


print(solve(board))
