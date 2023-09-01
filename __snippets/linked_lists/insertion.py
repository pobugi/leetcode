from base import weekdays_linked_list, Node


curr = weekdays_linked_list.root
while curr:
    if curr.value == "Wednesday":
        old_next = curr.next
        node = Node(value="blabla")
        curr.next = node
        node.next = old_next
        break
    curr = curr.next

weekdays_linked_list.print()