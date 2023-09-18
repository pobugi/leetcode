def solve(nums: list, target: int):
    min_lens = []

    for i in range(len(nums)):
        curr_len = 1
        sum = nums[i]
        j = i + 1
        while j < len(nums) and sum < target:
            sum += nums[j]
            j += 1
            curr_len += 1
        if sum >= target:
            min_lens.append(curr_len)
    return min(min_lens) if min_lens else 0


print(solve([2, 3, 1, 2, 4, 3], 7))
print(solve([1, 1, 1, 1], 7))
