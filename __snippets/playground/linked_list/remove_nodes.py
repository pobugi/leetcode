# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"


class SingleLinkedList:
    def __init__(self):
        self.root: Node | None = None

    def print(self):
        curr = self.root
        while curr:
            print(curr, end=", ")
            if curr.next == self.root:
                break
            curr = curr.next
        print()

    def remove(self, value: int):
        curr = self.root
        prev = None
        while curr:
            next = curr.next
            if curr.value == value:
                prev.next = curr.next
            prev = curr
            curr = curr.next
        self.print()



ll = SingleLinkedList()

[1,2,6,3,4,5,6]
node_1 = Node(value=1)
node_2 = Node(value=2)
node_3 = Node(value=3)
node_4 = Node(value=4)
node_5 = Node(value=5)
node_6_1 = Node(value=6)
node_6_2 = Node(value=6)

ll.root = node_1
ll.root.next = node_2
node_2.next = node_6_1
node_6_1.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6_2

ll.print()
ll.remove(value=6)