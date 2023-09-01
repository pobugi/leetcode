nums = [-4, -1, 0, 3, 10]


def solve(nums):
    result = []
    i = 0
    j = len(nums) - 1

    while i <= j:
        if (nums[i]) ** 2 > (nums[j]) ** 2:
            result = result + [(nums[i]) ** 2]
            i += 1
        else:
            result.insert(0, (nums[j]) ** 2)
            j -= 1
        print(f"nums[i]: {nums[i]}")
        print(f"nums[j]: {nums[j]}")
        print(result)

    return result


print(solve(nums))
