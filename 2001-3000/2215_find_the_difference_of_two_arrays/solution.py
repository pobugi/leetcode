# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]


def solve(nums1, nums2):
    hash_set1, hash_set2 = set(nums1), set(nums2)

    res1 = [num for num in hash_set1 if num not in hash_set2]
    res2 = [num for num in hash_set2 if num not in hash_set1]
    return res1, res2


print(solve([1, 2, 3, 3], [1, 1, 2, 2]))
