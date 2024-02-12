from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return str(self.val)


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            result = [curr.val] + result
            if curr.children:
                stack.extend(curr.children)
        return result


root = Node(1)
node2, node3, node4, node5, node6 = Node(2), Node(3), Node(4), Node(5), Node(6)
root.children = [node3, node2, node4]
node3.children = [node5, node6]

print(Solution().postorder(root))
