nums = [1, 7, 3, 6, 5, 6]


def solve(nums: list):
    i = 0

    while i < len(nums):

        sum_left = sum(nums[:i])
        sum_right = sum(nums[i + 1 :])
        if sum_left == sum_right:
            return i
        i += 1

    return -1


print(solve(nums))
