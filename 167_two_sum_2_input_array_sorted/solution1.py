from typing import List, Optional


def solution(nums: List[int], target: int) -> Optional[List[int]]:

    for i in range(len(nums)):
        left = i
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1
    return []


assert solution(nums=[2, 7, 11, 15], target=9) == [1, 2]
assert solution(nums=[2, 3, 4], target=6) == [1, 3]
assert solution(nums=[-19, -18, -10, -1], target=-19) == [2, 4]
print("solved!")
