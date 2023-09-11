"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def solution(nums: list):
    prefixes = [1]
    for i in range(len(nums) - 1):
        prefixes.append(nums[i] * prefixes[-1])

    postfixes = [1]
    for i in range(len(nums) - 1, 0, -1):
        postfixes = [postfixes[0] * nums[i]] + postfixes

    result = []
    for i in range(len(prefixes)):
        result.append(prefixes[i] * postfixes[i])
    return result


print(solution([1, 2, 3, 4]))
print(solution([-1, 1, 0, -3, 3]))
print(solution([4, 5, 1, 8, 2]))
