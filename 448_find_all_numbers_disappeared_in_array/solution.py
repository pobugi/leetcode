nums = [4, 3, 2, 7, 8, 2, 3, 1]


def solve(nums):
    dct = {
        key: 1 for key in range(1, len(nums) + 1)
    }

    for num in nums:
        dct.pop(num, None)

    return list(dct.keys())

print(solve(nums))
