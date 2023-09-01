# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
from time import sleep

arr = [5, 7, 7, 8, 8, 10]
target = 8


def solve(arr, target):
    # find the first occurence

    first = binary_search(arr, target)
    if first == -1:
        return [-1, -1]
    while True:
        result = binary_search(arr, target, end=first-1)
        if result == -1:
            break
        else:
            first = result

    second = first
    while True:
        result = binary_search(arr, target, start=second+1)
        if result == -1:
            break
        else:
            second = result
    if first == second:
        return [-1, -1]

    return [first, second]


def binary_search(arr, target, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return - 1


print(solve([1, 2, 3, 4, 4, 4, 5, 6, 7], 4))
print(solve([0,0,1,0,0], 1))
