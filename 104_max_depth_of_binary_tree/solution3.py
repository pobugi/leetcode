# Definition for a binary tree node.
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

        def height(node: TreeNode, level: int, levels: defaultdict) -> None:
            if not node: return
            levels[level].append(node.val)
            height(node.left, level + 1, levels)
            height(node.right, level + 1, levels)

        height(root, 0, levels)
        return len(levels)


root = TreeNode(3)
root.left, root.right = TreeNode(9), TreeNode(20)
root.right.left, root.right.right = TreeNode(15), TreeNode(7)

print(Solution().maxDepth(root))
