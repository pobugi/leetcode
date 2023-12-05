nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    i = 1
    curr = nums[0]
    while i < len(nums):
        while i < len(nums) and nums[i] == curr:
            nums.pop(i)
        if i >= len(nums):
            break
        curr = nums[i]
        i += 1
    return nums


print(removeDuplicates([1, 1]))
