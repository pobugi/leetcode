class Node:
    def __init__(self, value=0):
        self.value = value
        self.left: "Node | None" = None
        self.right: "Node | None" = None

    def __str__(self):
        return f"{self.value if self else None}"


root = Node(6)
root.left = Node(7)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(7)
root.left.left.left = Node(9)
root.left.right.left = Node(1)
root.left.right.right = Node(4)
root.right.left = Node(1)
root.right.right = Node(3)
root.right.right.right = Node(5)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Node) -> int:
        return self.dfs(root=root, parent=None, grand_parent=None)

    def dfs(self, root: Node | None, parent: Node | None, grand_parent: Node | None) -> int:
        if not root:
            return 0
        curr_sum = root.value if grand_parent and grand_parent.value % 2 == 0 else 0
        return (
            curr_sum
            + self.dfs(root=root.left, parent=root, grand_parent=parent)
            + self.dfs(root=root.right, parent=root, grand_parent=parent)
        )


print(Solution().sumEvenGrandparent(root))
