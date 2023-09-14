class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


def is_palindrome(arr: list):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True


node1 = Node(val=1)
node2 = Node(val=2)
node3 = Node(val=2)
node4 = Node(val=1)
node5 = Node(val=1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(is_palindrome(node1.to_list()))
