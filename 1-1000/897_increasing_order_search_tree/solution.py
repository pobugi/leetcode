class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(-1)
        curr = dummy
        tree = self.tree_to_list(root)
        for node in tree:
            dummy.right = TreeNode(val=node)
        return dummy.right

    def tree_to_list(self, root: TreeNode | None) -> list:
        result = []

        def inorder(root: TreeNode | None):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


root = TreeNode(5)
root.left = TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4))
root.right = TreeNode(6, right=TreeNode(8, left=TreeNode(7), right=TreeNode(9)))
