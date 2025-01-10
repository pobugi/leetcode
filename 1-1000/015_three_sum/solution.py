nums = [-1, 0, 1, 2, -1, -4, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]


def three_sum(nums):
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if num + nums[left] + nums[right] < 0:
                left += 1

            elif num + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result


print(three_sum(nums))
