class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_coordinates = sorted([point[0] for point in points], reverse=True)

        max_width = 0
        for i in range(len(x_coordinates) - 1):
            max_width = max(x_coordinates[i] - x_coordinates[i + 1], max_width)
        return max_width


print(Solution().maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))
