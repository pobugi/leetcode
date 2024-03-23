from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hash = self.get_dict(head)
        left = 1
        right = len(hash.keys()) - 1

        curr = head
        while left <= right:
            r = hash.get(right)
            if r:
                curr.next = r
                curr = r

            l = hash.get(left)
            if l:
                curr.next = l
                curr = l
            left += 1
            right -= 1
        curr.next = None

    def get_dict(self, head: ListNode | None):
        result = {}
        if not head:
            return result
        i = 0
        while head:
            result[i] = head
            head = head.next
            i += 1
        return result


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
