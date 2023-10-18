# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def solve(nums: list[int]) -> list[int]:
    # prefixes
    prefixes = [1]
    for num in nums[:-1]:
        prefixes.append(prefixes[-1] * num)
    # postfixes
    postfixes = [1]
    for num in nums[-1 : -len(nums) : -1]:
        postfixes = [postfixes[0] * num] + postfixes

    for i in range(len(prefixes)):
        prefixes[i] *= postfixes[i]
    return prefixes


print(solve([1, 2, 3, 4]))
