class Node:
    def __init__(self, value=0):
        self.val = value
        self.left: Node | None = None
        self.right: Node | None = None


root = Node(4)
root.left = Node(9)
root.left.left = Node(5)
root.left.right = Node(1)
root.right = Node(0)


def solve(root: Node | None):
    def dfs(node: Node | None, num: int):
        if not node:
            # just an edge case: if initial root is None
            return 0
        num = 10 * num + node.val
        if not node.left and not node.right:  # node is leaf
            return num
        return dfs(node.left, num) + dfs(node.right, num)

    # call dfs() for root with current num=0
    return dfs(root, 0)


print(solve(root))
