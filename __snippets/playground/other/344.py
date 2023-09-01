# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
s = ["H", "a", "n", "n", "a", "h"]


def reverse_string(s):
    end = len(s) - 1
    for i in range(end, -1, -1):
        s.append(s[i])
        print(s)
    s = s[end + 1:]
    print(s)

def reverse_2(s: list):

    end = len(s) - 1
    for i in range(end, -1, -1):
        s.append(s[i])
        s.pop(i)
        print(s)


    # print(s[end + 1:])
    # print(s)

reverse_2(s)