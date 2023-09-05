from typing import List, Optional


def solution(nums: List[int], target: int) -> Optional[List[int]]:
    def binary_search(arr, target, start):
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    for i in range(len(nums)):
        res = binary_search(nums, target - nums[i], i + 1)
        if res > -1:
            result = [i + 1, res + 1]
            return result
    return []


assert solution(nums=[2, 7, 11, 15], target=9) == [1, 2]
assert solution(nums=[2, 3, 4], target=6) == [1, 3]
assert solution(nums=[-19, -18, -10, -1], target=-19) == [2, 4]
print("solved!")
