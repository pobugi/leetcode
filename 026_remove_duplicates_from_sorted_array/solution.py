nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def solve(nums: list):
    i = 0
    j = 1

    while i < len(nums) and j < len(nums):
        curr = nums[i]
        while j < len(nums) and nums[j] == curr:
            nums.pop(j)
        i += 1
        j = i + 1


solve(nums)
