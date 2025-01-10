class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)


def is_symmetric(root: Node | None):
    if not root:
        return True
    return compare(root.left, root.right)


def compare(node1: Node | None, node2: Node | None):
    if not node1 and not node2:
        return True
    if node1 and not node2:
        return False
    if node2 and not node1:
        return False
    if node1.val != node2.val:
        return False
    return compare(node1.left, node2.right) and compare(node1.right, node2.left)


print(is_symmetric(root))
