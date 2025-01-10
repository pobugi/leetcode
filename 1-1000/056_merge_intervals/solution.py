from typing import List

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]


def solve(intervals: List[List[int]]):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]

        # if merge is necessary:
        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    return result


print(solve([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solve([[1, 3], [8, 10], [15, 18], [2, 6]]))
print(solve([[1, 3], [2, 6], [8, 10], [15, 18], [2, 6]]))
