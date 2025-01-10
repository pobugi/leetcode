nums = [1, 0, 1, 0, 1]
goal = 2


def solve(nums: list[int], goal: int):
    count = {0: 1}
    cumulative_sum = 0
    result = 0
    for num in nums:
        cumulative_sum += num
        if cumulative_sum - goal in count:
            result += count[cumulative_sum - goal]
        count[cumulative_sum] = count.get(cumulative_sum, 0) + 1
    return result


print(solve(nums, goal))
