class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node: {self.value}"


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


linked_list = SingleLinkedList()

monday = Node(value="Monday")
tuesday = Node(value="Tuesday")
wednesday = Node(value="Wednesday")
thursday = Node(value="Thursday")
friday = Node(value="Friday")
saturday = Node(value="Saturday")
sunday = Node(value="Sunday")

linked_list.root = monday
monday.next = tuesday
tuesday.next = wednesday
wednesday.next = thursday
thursday.next = friday
friday.next = saturday
saturday.next = sunday
sunday.next = monday

linked_list.print()
