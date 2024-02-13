from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)

        def height(node: TreeNode | None, level: int, levels: defaultdict):
            if not node:
                return
            levels[level].append(node.val)
            height(node.left, level + 1, levels)
            height(node.right, level + 1, levels)

        height(root, 0, levels)
        return max(levels.keys()) + 1 if levels else 0
