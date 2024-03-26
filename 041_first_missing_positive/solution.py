def solve(nums: list[int]):
    if not nums:
        return 1
    rng = [i for i in range(1, len(nums) + 2)]
    rng = set(rng)
    for num in nums:
        if num in rng:
            rng.remove(num)
    return list(rng)[0]


print(solve([1, 2, 0]))
print(solve([3, 4, -1, 1, 1, 2]))
print(solve([7, 8, 9, 11, 12]))
print(solve([1, 1]))
print(solve([1]))
