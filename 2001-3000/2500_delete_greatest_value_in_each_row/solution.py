class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for line in grid:
            line.sort()

        return sum(max([line[i] for line in grid]) for i in range(len(grid[0]) - 1, -1, -1))
