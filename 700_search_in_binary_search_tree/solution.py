# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


# root = [4, 2, 7, 1, 3]
# val = 2

root = Node(val=4)
root.left = Node(val=2)
root.left.left = Node(val=1)
root.left.right = Node(val=3)
root.right = Node(val=7)


def find(node: Node, val: int):
    if node is None:
        return None
    if node.val == val:
        return node
    if val > node.val:
        return find(node.right, val)
    return find(node.left, val)


print(find(root, 29))
