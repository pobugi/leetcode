nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]


def solve(nums, k):
    if not nums:
        return nums
    k = k % len(nums)

    end = nums[-k:]
    start = nums[:-k]
    return end + start


print(solve(nums, k))
