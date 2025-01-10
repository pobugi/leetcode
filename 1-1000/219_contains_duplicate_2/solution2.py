from typing import List
from collections import defaultdict

# nums, k

# 1. nums[i] == nums[j]
# 2. abs(i - j) <= k

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_indexes = self.make_dict(nums)  # convert nums into a dict: {value: [index1, index3, ...]}

        for val in value_indexes:
            if len(value_indexes[val]) < 1:  # it means that nums has no duplicate values
                continue
            lst = value_indexes[val]
            for i in range(1, len(lst)):
                if abs(lst[i] - lst[i - 1]) <= k:
                    return True
        return False

    def make_dict(self, nums: List[int]):
        # converts list of integers into a dict of a format: {value: [indexes]}
        # key: value, value: list of indexes of that value
        result = defaultdict(list)
        for i in range(len(nums)):
            value = nums[i]
            result[value].append(i)
        return result


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], k=3))
print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
