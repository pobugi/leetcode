def solve(path: str):
    stack = []
    curr = ""

    for letter in path + "/":
        if letter == "/":
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr not in ["", "."]:
                stack.append(curr)
            curr = ""
        else:
            curr += letter
    return "/" + "/".join(stack)


print(solve("/../abc/./def/"))
print(solve("/home/"))
print(solve("/../"))
print(solve("/home//foo/"))
print(solve("/a//b////c/d//././/.."))
