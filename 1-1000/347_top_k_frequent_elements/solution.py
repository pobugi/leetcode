nums = [1, 1, 1, 17, 17, 17, 2, 2, 3]


def solve(nums: list[int], n):
    result = {i: [] for i in range(1, len(nums) + 1)}
    counts = {}
    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    for num, count in counts.items():
        result[count].append(num)

    output = []
    for key in reversed(result.keys()):
        for x in result[key]:
            output.append(x)
            if len(output) >= n:
                return output


print(solve(nums, 2))
