from base import weekdays_linked_list, Node

curr = weekdays_linked_list.root
prev = None
while curr:
    if curr.value == "Wednesday" and prev:
        prev.next = curr.next

    prev = curr
    curr = curr.next

weekdays_linked_list.print()
