class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class SingleLinkedList:
    def __init__(self):
        self.root = None

    def print(self):
        visited = []

        curr = self.root
        while curr:
            print(curr)
            visited.append(curr)
            curr = curr.next
        print("------------------")
        print(f"Visited nodes: {visited}")
        print("------------------")

    def has_circles(self):
        visited = []

        curr = self.root
        while curr:
            if curr in visited:
                print(f"List is circled on node: {curr}")
                return True
            visited.append(curr)
            curr = curr.next
        return False


linked_list = SingleLinkedList()

monday = Node(value="Monday")
tuesday = Node(value="Tuesday")
wednesday = Node(value="Wednesday")
thursday = Node("Thursday")
friday = Node("Friday")
saturday = Node("Saturday")
sunday = Node("Sunday")

monday.next = tuesday
tuesday.next = wednesday
wednesday.next = thursday
thursday.next = friday
friday.next = saturday
saturday.next = sunday
sunday.next = monday

linked_list.root = monday

# linked_list.print()
print(linked_list.has_circles())