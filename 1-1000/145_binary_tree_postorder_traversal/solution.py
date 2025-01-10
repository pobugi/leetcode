# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        result = []

        def postorder(root):

            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        postorder(root)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().postorderTraversal(root))