import heapq


def solve(nums: list):
    result = []
    heapq.heapify(nums)
    while nums:
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        result.append(second)
        result.append(first)
    return result


print(solve([5, 4, 2, 3]))
