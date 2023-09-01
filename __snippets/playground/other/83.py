# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
    def deleteDuplicates(self, head):
        uniques = []
        curr = head
        prev = None
        while curr:
            if curr.val in uniques:
                print(f"{curr.val} to delete")
                prev.next = curr.next
                curr = curr.next
            else:
                uniques.append(curr.val)
                curr = curr.next
            prev = curr

    def print(self, head):
        curr = head
        prev = None
        while curr:
            print(f"{curr} (prev: {prev})", end=" ")
            prev = curr
            curr = curr.next
        print()

    def delete_node(self, node):
        pass


head = ListNode(val=1)

child1 = ListNode(val=1)
head.next = child1

child2 = ListNode(val=2)
child1.next = child2

child3 = ListNode(val=3)
child2.next = child3

child4 = ListNode(val=3)
child3.next = child4

s = Solution()
s.print(head)
# s.deleteDuplicates(head)
# s.print(head)

# head = [1, 1, 2, 3, 3]
# uniques = []
#
# for item in head:
#     if item in uniques:
#         print(f"{item} to delete")
#     else:
#         uniques.append(item)