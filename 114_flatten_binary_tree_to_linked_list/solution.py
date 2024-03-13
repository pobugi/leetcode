from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        self.dfs(root, arr)
        if root:
            root.left = None
        for node in arr[1:]:
            node.left = None
            root.right = node
            root = node

    def dfs(self, root: Optional[TreeNode], arr: list):
        if not root:
            return None
        arr.append(root)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

s = Solution()
print(s.flatten(root))
x = 4
assert True
