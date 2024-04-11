class Node:
    def __init__(self, value=0):
        self.val = value
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self):
        return f"{self.val if self else None}"


root = Node(2)
root.left = Node(1)
root.right = Node(4)
root.right.right = Node(5)


def add_value(node: Node | None, value: int):
    if not node:
        return Node(value)
    if value > node.val:
        if node.right:
            return add_value(node.right, value)
        else:
            node.right = Node(value)
    elif value < node.val:
        if node.left:
            return add_value(node.left, value)
        else:
            node.left = Node(value)

    else:
        raise ValueError("BST cannot have duplicates")


add_value(root, 3)
x = 1
