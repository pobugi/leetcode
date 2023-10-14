from typing import List

nums = [0, 1, 2, 4, 5, 7]


def gen(start: int):
    while True:
        yield start
        start += 1


def serialize(interval: List[int]) -> str:
    if not interval:
        return ""
    if len(interval) == 1:
        return str(interval[0])
    return f"{interval[0]}->{interval[-1]}"


def solve(nums: List[int]) -> List[str]:
    i = 0
    result = []
    while i < len(nums):
        g = gen(start=nums[i])
        sub_res = []
        while i < len(nums) and nums[i] == next(g):
            sub_res.append(nums[i])
            i += 1
        result.append(serialize(sub_res))
    return result


print(solve(nums))
