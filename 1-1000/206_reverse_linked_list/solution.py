class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    @staticmethod
    def print(node):
        curr = node
        while curr:
            print(curr.val)
            curr = curr.next

    @staticmethod
    def reverse(node):
        prev = node
        curr = node.next
        prev.next = None
        while curr:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
        return prev


monday = Node(val="monday")
tuesday = Node(val="tuesday")
wednesday = Node(val="wednesday")
thursday = Node(val="thursday")
friday = Node(val="friday")
saturday = Node(val="saturday")
sunday = Node(val="sunday")

monday.next = tuesday
tuesday.next = wednesday
wednesday.next = thursday
thursday.next = friday
friday.next = saturday
saturday.next = sunday

Node.reverse(monday)
Node.print(sunday)
