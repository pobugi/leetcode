from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = self.get_levels(root)
        return [levels[key][-1] for key in sorted(levels.keys())]

    def get_levels(self, root: TreeNode | None) -> defaultdict:
        levels = defaultdict(list)

        def dfs(root: TreeNode, level: int) -> None:
            if not root:
                return
            dfs(root.left, level + 1)
            levels[level].append(root.val)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return levels
