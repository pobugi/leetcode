class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        val = preorder.pop(0)
        index = inorder.index(val)
        left = inorder[:index]
        right = inorder[index + 1 :]
        root = TreeNode(val=val)
        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
res = Solution().buildTree(preorder, inorder)
print(res)
