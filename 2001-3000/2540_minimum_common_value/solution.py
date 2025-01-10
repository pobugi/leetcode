nums1 = [1, 2, 3]
nums2 = [2, 4]


def solve(nums1: list[int], nums2: list[int]):
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1


print(solve(nums1, nums2))
