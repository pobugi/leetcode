# https://leetcode.com/problems/valid-parentheses/description/


def solve(brackets):
    stack = []
    for bracket in brackets:
        if is_opening(bracket):
            stack.append(bracket)
        elif is_closing(bracket):
            if stack:
                last_bracket = stack[-1]
                if not is_matching(last_bracket, bracket):
                    return False
                else:
                    stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def is_matching(opening, closing):
    if opening == "{" and closing == "}":
        return True
    if opening == "(" and closing == ")":
        return True
    if opening == "[" and closing == "]":
        return True
    return False


def is_opening(bracket):
    if bracket in ("(", "[", "{"):
        return True
    return False


def is_closing(bracket):
    if bracket in (")", "]", "}"):
        return True
    return False


assert solve(brackets="()") is True
assert solve(brackets="()[]{}") is True
assert solve(brackets="(]") is False
print("success!")
