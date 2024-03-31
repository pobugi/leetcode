class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        postfixes = self.get_postfixes(root)

        def traverse(root: TreeNode | None):
            if root is None:
                return
            traverse(root.left)
            curr = postfixes.pop(0)
            root.val = curr
            traverse(root.right)

        traverse(root)
        return root

    def get_sum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return root.val + self.get_sum(root.left) + self.get_sum(root.right)

    def inorder(self, root: TreeNode | None) -> list[int]:
        result = []

        def traverse(root: TreeNode | None) -> None:
            if not root:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)

        traverse(root)
        return result

    def get_postfixes(self, root: TreeNode | None):
        flat_tree = self.inorder(root)
        total = sum(flat_tree)
        postfixes = [total]
        for value in flat_tree[:-1]:
            total -= value
            postfixes.append(total)
        return postfixes


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)

root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

s = Solution()
print(s.get_sum(root))
print(s.inorder(root))
print(s.get_postfixes(root))
