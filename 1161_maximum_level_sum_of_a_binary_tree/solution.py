from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        levels = defaultdict(int)

        def get_level(node: TreeNode | None, level: int, levels: defaultdict) -> None:
            if not node:
                return None
            levels[level] += node.val
            get_level(node.left, level + 1, levels)
            get_level(node.right, level + 1, levels)

        get_level(root, 1, levels)

        max_sum = max(levels.values())
        for level in levels:
            if levels[level] == max_sum:
                return level


root = TreeNode(1)
root.left = TreeNode(7)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right = TreeNode(0)

print(Solution().maxLevelSum(root))
