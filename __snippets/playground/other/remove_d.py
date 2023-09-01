nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4]

# i = 0
# j = 1
#
# while i < len(nums):
#     while True:
#         if j < len(nums) and nums[i] == nums[j]:
#             j += 1
#         else:
#             break
#     for k in range(i, j - 1):
#         nums.pop(k)
#     i += 1
#
# print(nums)

i = 1
while i < len(nums):
    print(nums)
    if nums[i] == nums[i-1]:
        nums.pop(i - 1)
    else:
        i += 1

print(nums)