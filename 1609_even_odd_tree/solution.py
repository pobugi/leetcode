from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)
        self.getLevels(root, levels, 0)
        print(levels)

        for key in levels:
            if not self.is_valid(key, values=levels[key]):
                return False
        return True

    def is_valid(self, level: int, values: list[int]) -> bool:
        if not values:
            return True
        if self.isEven(level):
            for value in values:
                if self.isEven(value):
                    return False
            if len(values) < 2:
                return True
            curr = values[0]
            for value in values[1:]:
                if value <= curr:
                    return False
                curr = value
            return True
        elif self.isOdd(level):
            for value in values:
                if self.isOdd(value):
                    return False
            if len(values) < 2:
                return True
            curr = values[0]
            for value in values[1:]:
                if value >= curr:
                    return False
                curr = value
            return True

        return False

    def isEven(self, num: int):
        return not bool(num % 2)

    def isOdd(self, num: int):
        return bool(num % 2)

    def getLevels(self, root: Optional[TreeNode], levels: defaultdict, level: int) -> None:
        if not root:
            return
        levels[level].append(root.val)
        self.getLevels(root.left, levels, level + 1)
        self.getLevels(root.right, levels, level + 1)
