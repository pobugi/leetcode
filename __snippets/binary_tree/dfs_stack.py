class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(value="D")

root.left = Node(value="B")
root.right = Node(value="F")

root.left.left = Node(value="A")
root.left.right = Node(value="C")

root.right.left = Node(value="E")


def dfs_stack(root: Node):
    result = []
    if not root:
        return result
    stack = [root]
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        result.append(current.value)
    return result

print(dfs_stack(root))