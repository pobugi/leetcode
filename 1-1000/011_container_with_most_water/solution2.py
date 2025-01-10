heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def solve(heights: list):
    start = 0
    end = len(heights) - 1
    max_volume = 0

    while start <= end:
        curr_volume = min(heights[start], heights[end]) * (end - start)
        max_volume = max(max_volume, curr_volume)
        if heights[start] > heights[end]:
            end -= 1
        else:
            start += 1
    return max_volume


print(solve(heights))
