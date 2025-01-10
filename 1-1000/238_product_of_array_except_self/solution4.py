# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def solve(nums):
    prefixes, postfixes = [1], [1]
    for num in nums[:-1]:
        prefixes.append(prefixes[-1] * num)

    for num in nums[(len(nums) - 1) : 0 : -1]:
        postfixes.append(postfixes[-1] * num)
    postfixes = postfixes[::-1]
    for i in range(len(prefixes)):
        prefixes[i] *= postfixes[i]
    return prefixes


print(solve([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(solve([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
