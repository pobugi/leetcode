class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"

    def print(self):
        curr = self
        while curr:
            print(curr.value)
            curr = curr.next

    def remove_duplicates(self):
        curr = self
        while curr:
            while curr.next and curr.next.value == curr.value:
                curr.next = curr.next.next
            curr = curr.next
        return head


head = Node(value=1)
node1 = Node(value=1)
head.next = node1
node2 = Node(value=1)
node1.next = node2
# node3 = Node(value=3)
# node2.next = node3
# node4 = Node(value=3)
# node3.next = node4
# node5 = Node(value=5)
# node4.next = node5
# node6 = Node(value=6)
# node5.next = node6

head.remove_duplicates()
head.print()
