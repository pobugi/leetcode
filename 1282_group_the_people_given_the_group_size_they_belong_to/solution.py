# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]

# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]
from collections import defaultdict


def solve(nums: list[int]):
    result = []
    dct = defaultdict(list)
    for i, num in enumerate(nums):
        dct[num].append(i)
    for key in dct:
        arr = dct[key]
        if len(arr) == key:
            result.append(arr)
        else:
            for i in range(len(arr) // key):
                result.append(arr[i * key : (i + 1) * key])
    return result


print(solve([3, 3, 3, 3, 3, 1, 3]))
print(solve([2, 1, 3, 3, 3, 2]))
