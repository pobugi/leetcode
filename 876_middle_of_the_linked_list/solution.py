class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
curr = head
for num in [2, 3, 4, 5]:
    curr.next = ListNode(num)
    curr = curr.next


def find_middle(root: ListNode):
    if not root:
        return None
    slow = root
    fast = root
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


mid = find_middle(head)
