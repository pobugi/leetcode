class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

class DoubleLinkedList:
    def __init__(self, root):
        self.root = root

    def print(self):
        curr = self.root
        while curr:
            print(curr)
            curr = curr.next

    def get_last_node(self):
        curr = self.root
        while curr:
            if curr.next is None:
                return curr
            curr = curr.next



mon = Node("Monday")
tue = Node("Tuesday")
wed = Node("Wednesday")
thu = Node("Thursday")
fri = Node("Friday")
sat = Node("Saturday")
sun = Node("Sunday")

mon.next = tue
tue.prev = mon
tue.next = wed
wed.prev = tue
wed.next = thu
thu.prev = wed
thu.next = fri
fri.prev = thu
fri.next = sat
sat.prev = fri
sat.next = sun
sun.prev = sat



week_list = DoubleLinkedList(root=mon)

week_list.print()

print(week_list.get_last_node())