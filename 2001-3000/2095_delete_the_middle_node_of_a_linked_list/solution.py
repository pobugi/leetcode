# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    @staticmethod
    def print(head):
        curr = head
        while curr:
            print(curr, end=" ")
            curr = curr.next
        print()

    @staticmethod
    def get_len(head):
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        return l

    @staticmethod
    def remove_middle(head):
        if head.next is None:
            return None
        middle = Node.get_len(head) // 2
        curr = head
        for i in range(middle - 1):
            curr = curr.next
        curr.next = curr.next.next


# head = [1,3,4,7,1,2,6]

head = Node(1)
node2 = Node(3)
head.next = node2
node3 = Node(4)
node2.next = node3
node4 = Node(7)
node3.next = node4
node5 = Node(1)
node4.next = node5
node6 = Node(2)
node5.next = node6
node7 = Node(6)
node6.next = node7

Node.print(head)

Node.remove_middle(head)

Node.print(head)
