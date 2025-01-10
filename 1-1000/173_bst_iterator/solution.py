from typing import Optional


class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = self.fill_stack(root)

    def next(self) -> int | None:
        if not self.stack:
            return None
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def fill_stack(self, root):
        stack = []

        def traversal(root: TreeNode | None):
            if not root:
                return
            traversal(root.left)
            stack.append(root.val)
            traversal(root.right)

        traversal(root)
        return stack


root = TreeNode(7)
root.left, root.right = TreeNode(3), TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)


iterator = BSTIterator(root)
print(iterator.hasNext())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
