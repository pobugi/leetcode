# Definition for singly-linked list.
from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode with value: {self.val}"

    def get_gepth(self, root):
        res = 0
        curr = root
        while curr.next:
            res += 1
            curr = curr.next
        return res

root = ListNode()
curr = root

for i in range(5):
    node = ListNode(val=randint(1, 10))
    print(node)
    curr.next = node
    curr = node


depth = root.get_gepth(root)
middle = depth // 2
print("---")
print(middle)
curr = root

for i in range(middle + 1):
    curr = curr.next
print("middle:")
print(curr)

# curr = root
# while curr.next:
#     print(curr)
#     print(f"current depth: {root.get_gepth(root)}")
#     curr = curr.next

