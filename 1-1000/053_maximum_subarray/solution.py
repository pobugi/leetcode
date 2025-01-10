nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def solve(nums: list[int]):
    max_sum = nums[0] if nums else 0
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        print(f"curr_sum: {curr_sum}")
        print(f"max_sum: {max_sum}")
        print()

    return max_sum


print(solve(nums))
