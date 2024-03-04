from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x1 == x2:
            for point in coordinates[1:]:
                if point[0] != x1:
                    return False
            return True

        if y1 == y2:
            for point in coordinates[1:]:
                if point[1] != y1:
                    return False
            return True

        ratio = (x2 - x1) / (y2 - y1)

        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            x1, y1 = coordinates[i - 1]
            if (x2 - x1) / (y2 - y1) != ratio:
                return False
        return True
