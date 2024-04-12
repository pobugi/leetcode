# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def permutations(nums: list[int]) -> list[list[int]]:
    result = []
    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        num = nums[i]
        other = nums[:i] + nums[i + 1 :]
        perms = permutations(other)
        for perm in perms:
            perm.append(num)
        result.extend(perms)
    return result


for p in permutations([1, 2, 3]):
    print(p)
