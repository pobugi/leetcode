# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


def generateParenthesis0(n: int):
    stack = []
    result = []

    def backtrack(open: int, closed: int):
        print(f"backtrack: {open}, {closed}")
        print(stack)
        print()
        if open == closed == n:
            result.append("".join(stack))
        if open < n:
            stack.append("(")
            backtrack(open + 1, closed)
            stack.pop()
        if closed < open:
            stack.append(")")
            backtrack(open, closed + 1)
            stack.pop()

    backtrack(0, 0)
    return result


def generateParenthesis(n: int) -> list[str]:
    res = []

    def backtrack(open_n, closed_n, path):
        print(f"backtrack: {open_n} {closed_n} {path}")
        if open_n == closed_n == n:
            res.append(path)
            return

        if open_n < n:
            backtrack(open_n + 1, closed_n, path + "(")

        if closed_n < open_n:
            backtrack(open_n, closed_n + 1, path + ")")

    backtrack(0, 0, "")
    return res


# print(generateParenthesis(3))


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(openN: int, closedN: int, path: str):
            if openN == closedN == n:
                result.append(path)
                return
            if openN < n:
                backtrack(openN + 1, closedN, path + "(")
            if closedN < openN:
                backtrack(openN, closedN + 1, path + ")")

        backtrack(0, 0, "")
        return result


print(Solution().generateParenthesis(3))
