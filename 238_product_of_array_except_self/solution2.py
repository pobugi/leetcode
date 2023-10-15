# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


def product(nums: list[int]):
    prefixes = [1]
    postfixes = [1]

    for i in range(len(nums) - 1):
        prefixes.append(prefixes[-1] * nums[i])
    for i in range(-1, -len(nums), -1):
        postfixes = [postfixes[0] * nums[i]] + postfixes

    return [x * y for x, y in zip(prefixes, postfixes)]


print(product([1, 2, 3, 4]))
print(product([-1, 1, 0, -3, 3]))
