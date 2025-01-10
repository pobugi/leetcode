# Input: preorder = [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode | None:
        if not preorder:
            return
        root_value = preorder[0]
        root = TreeNode(root_value)
        left_values = [num for num in preorder[1:] if num <= root_value]
        right_values = [num for num in preorder[1:] if num > root_value]
        root.left = self.bstFromPreorder(left_values)
        root.right = self.bstFromPreorder(right_values)
        return root


result = Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
