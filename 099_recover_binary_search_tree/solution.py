import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        flat = self.flatten(root)
        heapq.heapify(flat)

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            root.val = heapq.heappop(flat)
            traverse(root.right)

        traverse(root)

    def flatten(self, root: Optional[TreeNode]) -> list[int]:
        flat = []

        def dfs(node):
            if not node:
                return
            flat.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return flat


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

s = Solution()
print(s.recoverTree(root))
