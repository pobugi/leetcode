from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, value=0):
        self.val = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


root = TreeNode(3)
root.left, root.right = TreeNode(9), TreeNode(20)
root.right.left, root.right.right = TreeNode(15), TreeNode(7)


def get_average_of_levels(root: Optional[TreeNode]) -> List[float]:
    level_count_dict = defaultdict(int)
    level_sum_dict = defaultdict(int)

    def dfs(node: Optional[TreeNode], level: int):
        # print(f"call for node: {node.val if node else None}, level: {level}")
        if not node:
            return
        level_count_dict[level] += 1
        level_sum_dict[level] += node.val

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, level=0)
    return [level_sum_dict[level] / level_count_dict[level] for level in level_sum_dict]


print(get_average_of_levels(root))
