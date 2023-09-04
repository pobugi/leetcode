nums = [1, 2, 1]


def solve(nums):
    length = len(nums)
    for i in range(length):
        nums.append(nums[i])
    return nums


print(solve(nums))
