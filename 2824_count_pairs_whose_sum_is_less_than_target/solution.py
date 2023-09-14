nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2


nums.sort()
count = 0

for i in range(len(nums)):
    first = nums[i]
    remaining = nums[i + 1 :]
    j = 0
    while j < len(remaining) and first + remaining[j] < target:
        first = first
        rem = remaining[j]
        r = first + remaining[j]
        count += 1
        j += 1
print(count)
