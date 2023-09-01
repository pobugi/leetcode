# 20 valid parentheses
s = "()[]{}"


def is_opening(s):
    return s in ("(", "[", "{",)


def is_closing(s):
    return s in (")", "]", "}",)


for letter in s:
    print("is")