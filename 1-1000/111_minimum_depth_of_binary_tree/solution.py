from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depths = []

        def dfs(node: TreeNode | None, depth: int):
            if not node:
                return
            depth += 1
            if not node.left and not node.right:
                depths.append(depth)
                depth -= 1
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)
        return min(depths) if depths else 0


root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(66)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(17)

print(Solution().minDepth(root))
