from typing import List


def binary_search(nums: list[int], target: int, start=None, end=None) -> int:
    start = 0 if start is None else start
    end = len(nums) - 1 if end is None else end

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def solve(nums: List[int], target: int) -> List[int]:
    start = 0
    end = len(nums) - 1

    # find first

    first = binary_search(nums, target)  # find item in the whole array
    # if it is not found, then both, first and last = -1:
    if first == -1:
        return [-1, -1]

    # shrink from right to left to find the leftmost occurence:
    while True:
        res = binary_search(nums, target, start, first - 1)
        if res == -1:
            break
        else:
            first = res

    # find last

    last = binary_search(nums, target, start=first)  # find item in array starting from left index
    if last == -1:
        return [first, -1]

    # shrink from left to right to find the rightmost occurence:
    while True:
        res = binary_search(nums, target, last + 1, end)
        if res == -1:
            break
        else:
            last = res

    return [first, last]


nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8

print(solve(nums, target))

nums = [1]
target = 1

print(solve(nums, target))
