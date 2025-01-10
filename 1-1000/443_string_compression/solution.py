chars = ["x", "a", "a", "b", "b", "c", "c", "c", "d", "e"]
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]


def solve(chars: list):

    i = 1
    count = 1
    while i < len(chars):
        while i < len(chars) and chars[i] == chars[i - 1]:
            count += 1
            chars.pop(i - 1)
        if count > 1:
            if count > 9:
                for digit in str(count):
                    chars.insert(i, digit)
                    i += 1
                i += 1
            else:
                chars.insert(i, str(count))
                i += 2
        else:
            i += 1
        count = 1

    return chars


print(solve(chars))
