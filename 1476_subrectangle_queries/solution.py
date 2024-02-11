from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def __str__(self):
        return str(self.rectangle)

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


rectangle = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
rectangle.updateSubrectangle(0, 0, 3, 2, 5)
print(rectangle)
