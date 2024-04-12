def generate_parentheses(n: int) -> list[str]:
    result = []

    def helper(openN: int, closedN: int, path: list):
        if openN == closedN == n:
            result.append(path.copy())
            return
        if closedN < openN:
            path.append(")")
            helper(openN, closedN + 1, path)
            path.pop()
        if openN < n:
            path.append("(")
            helper(openN + 1, closedN, path)
            path.pop()

    helper(0, 0, [])
    return ["".join(r) for r in result]


print(generate_parentheses(3))
