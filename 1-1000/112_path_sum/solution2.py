from typing import Optional


class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(12)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(14)
root.right.right.right = TreeNode(1)


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root: TreeNode | None, currSum: int):
        if not root:
            return False
        currSum += root.val
        print(f"node: {root.val if root else None}; currSum: {currSum}")
        if not root.left and not root.right:
            return currSum == targetSum
        return dfs(root.left, currSum) or dfs(root.right, currSum)

    return dfs(root, 0)


print(hasPathSum(root, 22))
