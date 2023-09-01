# merge
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node with val: {self.val}"


class SingleLinkedList:
    def __init__(self):
        self.root = None

    def print(self):
        curr = self.root
        while curr:
            print(curr)
            if curr.next == self.root:
                break
            curr = curr.next


list1 = [1, 2, 4]
list2 = [1, 3, 4]

# list1:
lst1 = SingleLinkedList()
root1 = ListNode(val=1)
lst1.root = root1
child1 = ListNode(val=2)
root1.next = child1
child2 = ListNode(val=4)
child1.next = child2

# list2:

lst2 = SingleLinkedList()
root21 = ListNode(val=1)
lst2.root = root21

child21 = ListNode(val=3)
root21.next = child21

child22 = ListNode(val=4)
child21.next = child22


# lst1.print()
# print("------")
# lst2.print()


def mergeTwoLists(list1: ListNode, list2: ListNode):

    curr1 = list1
    curr2 = list2
    res_root = ListNode()

    if curr1.val > curr2.val:
        res_root.val = curr2.val
        curr2 = curr2.next
    else:
        res_root.val = curr1.val
        curr1 = curr1.next


    res_curr = ListNode()
    res_root.next = res_curr

    while curr1 and curr2:
        if curr1.val > curr2.val:
            res_curr.val = curr2.val
            curr2 = curr2.next
        else:
            res_curr.val = curr1.val
            curr1 = curr1.next

    while curr1.next and curr2.next:

        if curr1.val < curr2.val:
            res_root.val = curr1.val
            curr1 = curr1.next
        else:
            res_root.val = curr2.val
            curr2 = curr2.next

    return res_root


res = mergeTwoLists(root1, root21)
l = SingleLinkedList()
l.root = res
l.print()