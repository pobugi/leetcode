from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {
            "++X": lambda x: x + 1,
            "X++": lambda x: x + 1,
            "--X": lambda x: x - 1,
            "X--": lambda x: x - 1,
        }

        value = 0

        for operation in operations:
            value = ops[operation](value)
        return value
