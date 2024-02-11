class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        children = root.children
        if not children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)


node1 = Node(val=1)
node2 = Node(val=2)
node3 = Node(val=3)
node4 = Node(val=4)
node5 = Node(val=5)
node6 = Node(val=6)

node1.children = [node2, node3, node4]
node3.children = [node5, node6]

print(Solution().maxDepth(node1))
