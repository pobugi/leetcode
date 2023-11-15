from models.list_node import ListNode

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)


def solve(head: ListNode | None, x: int):
    left = ListNode()
    right = ListNode()
    left_root = left
    right_root = right

    curr = head
    while curr:
        if curr.val < x:
            left.next = curr
            left = left.next
        else:
            right.next = curr
            right = right.next
        curr = curr.next
    left.next = None
    right.next = None
    left.next = right_root.next
    return left_root.next


res = solve(head, 3)
ListNode.print_list(res)
