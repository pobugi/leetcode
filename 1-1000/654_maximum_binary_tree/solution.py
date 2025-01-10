from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


nums = [3, 2, 1, 6, 0, 5]


def split_list(nums: List[int]):
    print(f"split nums: {nums}")
    # find max index:
    if not nums:
        return None
    if len(nums) == 1:
        return [], nums[0], []

    curr_max = max(nums)
    i = nums.index(curr_max)
    result = nums[:i], curr_max, nums[i + 1 :]
    return result


root = TreeNode()


def build_tree(root, nums):
    if not nums:
        return
    left_values, root_value, right_values = split_list(nums)
    root.val = root_value
    print(f"call for: {root.val if root else None} {nums}")
    if left_values:
        root.left = TreeNode()
        build_tree(root.left, left_values)
    if right_values:
        root.right = TreeNode()
        build_tree(root.right, right_values)


res = build_tree(root, nums)
