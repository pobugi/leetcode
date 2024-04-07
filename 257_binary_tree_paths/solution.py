from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node: Optional[TreeNode], path: str):
            if not node:
                return

            path += "->" + str(node.val) if path else str(node.val)
            if not node.left and not node.right:
                paths.append(path)

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return paths


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

s = Solution()
print(s.binaryTreePaths(root))
