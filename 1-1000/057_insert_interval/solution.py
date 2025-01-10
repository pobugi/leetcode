# Input: intervals = [[1,3], [6,9]], newInterval = [2,5]
# Output: [[1,5], [6,9]]


def solve(intervals: list[list[int]], new_interval: list[int]):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]

        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])
    return result


print(solve([[1, 3], [6, 9]], [2, 5]))
