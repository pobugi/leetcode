class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        while curr.next:
            next = curr.next
            if next.next is None:
                curr.val = next.val
                curr.next = None
                break
            curr.val = next.val
            curr = curr.next


node4 = ListNode(4)
node5 = ListNode(5)
node4.next = node5
node1 = ListNode(1)
node5.next = node1
node9 = ListNode(9)
node1.next = node9


def print_list(node: ListNode | None):
    if not node:
        return
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


print_list(node4)
Solution().deleteNode(node5)
print_list(node4)
