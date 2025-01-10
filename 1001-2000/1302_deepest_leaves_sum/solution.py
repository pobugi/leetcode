from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict

        levels = defaultdict(list)
        self.dfs_with_levels(root, 0, levels)

        max_depth = self.get_max_depth(root)
        return sum(levels[max_depth - 1])

    def dfs_with_levels(self, root: TreeNode | None, level: int, result: defaultdict):
        if not root:
            return result
        result[level].append(root.val)
        self.dfs_with_levels(root.left, level + 1, result)
        self.dfs_with_levels(root.right, level + 1, result)

    def get_max_depth(self, root: TreeNode | None):
        if not root:
            return 0
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))
