from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        results = []

        def helper(root: Optional[TreeNode], results: list[int]):
            if not root:
                return 0
            left = self.get_depth(root.left)
            right = self.get_depth(root.right)
            results.append(left + right)
            helper(root.left, results)
            helper(root.right, results)

        helper(root, results)
        return max(results)

    def get_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))


root = TreeNode(4)
root.left = TreeNode(-7)
root.right = TreeNode(-3)

root.right.right = TreeNode(-3)
root.right.right.left = TreeNode(-4)

root.right.left = TreeNode(-9)
root.right.left.left = TreeNode(9)
root.right.left.left.left = TreeNode(6)
root.right.left.left.left.left = TreeNode(0)
root.right.left.left.left.right = TreeNode(6)
root.right.left.left.left.left.right = TreeNode(-1)
root.right.left.left.left.right.left = TreeNode(-4)

root.right.left.right = TreeNode(-7)
root.right.left.right.left = TreeNode(-6)
root.right.left.right.left.left = TreeNode(5)
root.right.left.right.right = TreeNode(-6)
root.right.left.right.right.left = TreeNode(9)
root.right.left.right.right.left.left = TreeNode(-2)

s = Solution()
print(s.diameterOfBinaryTree(root))
