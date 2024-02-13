from collections import defaultdict


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_levels(node: Node | None, level: int, levels):
    if not node:
        return
    levels[level].append(node.val)
    dfs_levels(node.left, level + 1, levels)
    dfs_levels(node.right, level + 1, levels)


def get_max_depth(node: Node | None) -> int:
    if not node:
        return 0
    return 1 + max(get_max_depth(node.left), get_max_depth(node.right))


def solve(node: Node | None) -> int:
    levels = defaultdict(list)
    dfs_levels(node, 1, levels)
    max_depth = get_max_depth(node)
    return sum(levels[max_depth])
