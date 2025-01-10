from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation[-1].isdigit():
                stack.append(int(operation))
            elif operation == "+":
                last = stack.pop()
                pre_last = stack.pop()
                new_score = last + pre_last
                stack.append(pre_last)
                stack.append(last)
                stack.append(new_score)
            elif operation.lower() == "d":
                stack.append(stack[-1] * 2)
            elif operation.lower() == "c":
                stack.pop()

        return sum(stack)


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
