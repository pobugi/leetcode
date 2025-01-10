class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
"""


class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return bool(root.val)
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return True


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(Solution().evaluateTree(root))
