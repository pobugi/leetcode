from typing import Optional


class Node:
    def __init__(self, value=0):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(8)

root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)


def post_order(root: Optional[Node]):
    if not root:
        return None
    print(root.value, end=" ")
    post_order(root.left)
    post_order(root.right)


post_order(root)
