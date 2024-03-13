# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=" ")
            head = head.next
        print()


s = Solution()
head = [1, 2, 3, 4, 5]
n = 2

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
s.printList(root)
s.removeNthFromEnd(root, 2)
s.printList(root)
