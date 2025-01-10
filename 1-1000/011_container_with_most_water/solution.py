"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1
"""

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def solve(heights: list):
    left = 0
    right = len(heights) - 1

    max_square = 0

    while left < right:
        left_height = heights[left]
        right_height = heights[right]

        side = min(left_height, right_height)
        square = (right - left) * side
        max_square = max(square, max_square)
        if side == left_height:
            left += 1
        else:
            right -= 1
    return max_square


print(solve(heights))
