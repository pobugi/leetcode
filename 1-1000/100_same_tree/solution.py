from typing import Optional


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)


class Solution:
    def isSameTree(self, p: Optional[Node], q: Optional[Node]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


print(Solution().isSameTree(root1, root2))
