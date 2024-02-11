"""
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
"""

from typing import List


def solve(nums: List[int]):
    result = [[]]
    i = 0
    for num in nums:
        while num in result[i]:
            i += 1
            if i > len(result) - 1:
                result.append([])
        result[i].append(num)
        i = 0

    return result


print(solve([1, 3, 4, 1, 2, 3, 1]))
