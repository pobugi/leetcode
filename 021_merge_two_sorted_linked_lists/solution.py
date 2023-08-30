class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    @property
    def length(self):
        res = []
        curr = self
        while curr:
            res.append(curr)
            curr = curr.next
        return res


def print_list(root: ListNode):
    curr = root
    while curr:
        print(curr)
        curr = curr.next


list1 = [1, 2, 4]
list2 = [1, 3, 4]

# lst 1:
root1 = ListNode(val=1)
root1.next = ListNode(val=3)
root1.next.next = ListNode(val=4)

# lst 2:
root2 = ListNode(val=2)
root2.next = ListNode(val=5)
root2.next.next = ListNode(val=6)


def merge(root1: ListNode, root2: ListNode):
    res_root = ListNode(val=None)
    curr = res_root
    curr1 = root1
    curr2 = root2

    while curr1 and curr2:
        if curr1.val > curr2.val:
            curr.next = curr2
            curr2 = curr2.next
        else:
            curr.next = curr1
            curr1 = curr1.next
        curr = curr.next

    if curr1:
        curr.next = curr1
    if curr2:
        curr.next = curr2

    return res_root.next


print_list(merge(root1, root2))
