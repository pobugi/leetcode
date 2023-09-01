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

    def reverse(self):
        curr = self.root
        prev = None

        while True:
            if curr.next is None:
                break

            next = curr.next
            prev = curr

    def get_last(self):
        curr = self.root
        while True:
            if curr.next is None:
                return curr
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

linked_list.print()
last = linked_list.get_last()
print(last)