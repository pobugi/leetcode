class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(value=3)

root.left = Node(value=11)
root.left.left = Node(value=4)
root.left.right = Node(value=2)

root.right = Node(value=4)
root.right.right = Node(value=1)


def get_sum(root: Node) -> int:
    print(f"call get_sum for root: {root.value if root else None}")
    if not root:
        return 0
    return get_sum(root.left) + get_sum(root.right) + root.value


print(get_sum(root))
