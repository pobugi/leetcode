from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        levels = defaultdict(list)
        self.get_levels(root, levels, 0)
        deepest_level = max(levels.keys())
        return levels[deepest_level][0] if len(levels[deepest_level]) else None

    def get_levels(self, root: TreeNode | None, levels: defaultdict, level: int) -> defaultdict:
        if not root:
            return None
        levels[level].append(root.val)
        self.get_levels(root.left, levels, level + 1)
        self.get_levels(root.right, levels, level + 1)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.left = TreeNode(7)
root.right.right = TreeNode(6)

print(Solution().findBottomLeftValue(root))
