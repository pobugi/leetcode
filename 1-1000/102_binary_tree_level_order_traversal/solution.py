from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        result = defaultdict(list)

        def solve(root, level, result):
            if not root:
                return
            result[level].append(root.val)
            solve(root.left, level + 1, result)
            solve(root.right, level + 1, result)

        solve(root, 0, result)
        return list(result.values())
