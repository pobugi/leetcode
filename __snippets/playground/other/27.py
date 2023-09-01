nums = [0, 1, 2, 2, 3, 0, 4, 2, 2, 2, 2, 2, 2]
val = 2


def solve(nums, val):
    indexes = []
    for i in range(len(nums)):
        if nums[i] == val:
            indexes.append(i)
    incr = 0
    for index in indexes:
        nums.pop(index - incr)
        incr += 1

    return nums


print(solve(nums, val))