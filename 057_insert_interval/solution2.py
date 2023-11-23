# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]


def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    if not intervals:
        return [new_interval]
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result


# [[1, 5], [6, 9], [15, 18]]
print(solve([[1, 3], [15, 18], [6, 9]], [2, 5]))  # [[1, 5], []]
