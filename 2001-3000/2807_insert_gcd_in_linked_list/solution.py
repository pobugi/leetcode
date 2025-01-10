class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# head = [18, 6, 10, 3]  # [18,6,6,2,10,1,3]


head = Node(val=18)
head.next = Node(val=6)
head.next.next = Node(val=10)
head.next.next.next = Node(val=3)


def gcd(a: int, b: int) -> int:
    while a and b:
        a, b = min(a, b), max(a, b)
        b = b % a
    return a or b


curr = head
while curr and curr.next:
    temp = curr.next
    curr.next = Node(gcd(curr.val, curr.next.val))
    curr.next.next = temp
    curr = temp
