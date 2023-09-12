rows = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]


def solve(grid):
    cols = [[grid[j][i] for j in range(len(grid[i]))] for i in range(len(grid))]

    count = 0
    for row in grid:
        for col in cols:
            if row == col:
                count += 1

    return count
