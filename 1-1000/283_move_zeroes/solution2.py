nums = [0, 1, 0, 3, 12]  # [1,3,12,0,0]
nums = [0, 0, 1]  # [1,0,0]


def solve(nums: list[int]):
    zeros = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            zeros += 1
        else:
            i += 1
    nums.extend([0 for _ in range(zeros)])
    return nums


print(solve(nums))
