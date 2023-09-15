lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]

res = []


def merge(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    i = 0
    j = 0
    res = []
    while list1 and list2:
        if list1[i] < list2[j]:
            res.append(list1.pop(i))
        else:
            res.append(list2.pop(j))
    if list1:
        for i in range(len(list1)):
            res.append(list1.pop(i))
    else:
        for j in range(len(list2)):
            res.append(list2.pop(j))
    return res


def solve(lists):
    for i in range(1, len(lists)):
        curr = merge(lists[i], lists[i - 1])
        lists[i] = curr
    return curr


print(solve(lists))
