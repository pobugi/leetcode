from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) if self else None

    def __str__(self):
        return str(self.val) if self else None

    @staticmethod
    def print_list(root: Optional["ListNode"]):
        while root:
            print(root, end=" ")
            root = root.next
