arr = [1, 2, 3]


def get_subsets(nums: list[int]) -> list[list[int]]:
    result = []
    subset = []

    def dfs(i: int):
        if i >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result


print(get_subsets(arr))
