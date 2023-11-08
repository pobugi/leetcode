from typing import Optional


class Node:
    def __init__(self, value=0):
        self.val = value
        self.left: Node | None = None
        self.right: Node | None = None


root = Node(4)
root.left = Node(8)
root.right = Node(5)
root.left.left = Node(0)
root.left.right = Node(1)
root.right.right = Node(6)


def tree_average(root: Optional[Node]):
    total_count = 0
    total_sum = 0

    def solve(node: Optional[Node]):
        nonlocal total_count
        nonlocal total_sum
        if not node:
            return
        stack = [node]
        while stack:
            curr = stack.pop()
            total_count += 1
            total_sum += curr.val

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

    solve(root)
    return total_sum, total_count


print(tree_average(root))
