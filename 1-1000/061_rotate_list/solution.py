class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) if self else None


root = Node(val=1)
root.next = Node(val=2)
root.next.next = Node(val=3)
root.next.next.next = Node(val=4)
root.next.next.next.next = Node(val=5)


def rotate(root: Node | None, k: int = 0):
    if not root:
        return root

    length = 0
    curr = root
    while curr:
        curr = curr.next
        length += 1

    k = k % length
    if k == 0:
        return root

    curr = root
    for i in range(length - k - 1):
        curr = curr.next

    new_root = curr.next
    curr.next = None

    for i in range(k - 1):
        curr = new_root.next

    curr.next = root

    return new_root


new_root = rotate(root, 2)
x = 8
