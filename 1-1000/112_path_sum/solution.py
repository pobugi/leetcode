from typing import Optional


class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(4)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and root.val - targetSum == 0:
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


print(hasPathSum(root, 22))
