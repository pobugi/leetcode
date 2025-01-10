nums = [9, 9, 9, 9, 9]


def solve(nums: list[int]):
    carry = 1
    for i in range(len(nums) - 1, -1, -1):
        curr = nums[i] + carry
        carry = 0
        if curr >= 10:
            curr, carry = curr % 10, 1
        nums[i] = curr
    if carry:
        nums = [carry] + nums
    return nums


print(solve(nums))
