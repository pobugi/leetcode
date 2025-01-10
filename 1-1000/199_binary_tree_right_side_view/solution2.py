from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_levels(self, root):
        levels = defaultdict(list)

        def dfs(node, level, levels):
            if not node:
                return
            dfs(node.left, level + 1, levels)
            levels[level].append(node.val)
            dfs(node.right, level + 1, levels)

        dfs(root, 0, levels)
        print(levels)
        for i in range(len(levels)):
            if len(levels[i]):
                print(levels[i][-1])


root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        right=TreeNode(val=5)),
    right=TreeNode(
        val=3,
        right=TreeNode(val=4)
    ),
)
s = Solution()
print(s.get_levels(root))