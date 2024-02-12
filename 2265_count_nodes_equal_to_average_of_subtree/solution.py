class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = int(
            root.val == int(self.get_tree_sum(root) / self.get_tree_count(root))
        )
        return (
            result
            + self.averageOfSubtree(root.left)
            + self.averageOfSubtree(root.right)
        )

    def get_tree_sum(self, root: TreeNode | None):
        if not root:
            return 0
        return root.val + self.get_tree_sum(root.left) + self.get_tree_sum(root.right)

    def get_tree_count(self, root: TreeNode | None):
        if not root:
            return 0
        return 1 + self.get_tree_count(root.left) + self.get_tree_count(root.right)


print(Solution().averageOfSubtree(root))
