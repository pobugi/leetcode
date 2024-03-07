from itertools import permutations


def solve(num: int) -> int:
    nums = split_digit(num)
    nums.sort()

    result = ["", ""]

    result[0] += str(nums[0])
    result[1] += str(nums[1])
    result[0] += str(nums[2])
    result[1] += str(nums[3])
    return int(result[0]) + int(result[1])


def split_digit(num: int) -> list:
    res = []
    while num:
        res = [num % 10] + res
        num //= 10
    return res


print(solve(2932))
print(solve(4009))
