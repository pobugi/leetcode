def generate_parentheses(n: int) -> list[str]:
    result = []

    def backtrack(openN: int, closedN: int, path: str):
        if openN == closedN == n:
            result.append(path)

        if openN < n:
            backtrack(openN + 1, closedN, path + "(")
        if closedN < openN:
            backtrack(openN, closedN + 1, path + ")")

    backtrack(0, 0, "")
    return result


print(generate_parentheses(3))
