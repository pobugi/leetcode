# Definition for singly-linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def has_cycle(self):
        visited = set()
        curr = self
        while curr:
            if curr.next is None:
                return False
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next


mon = Node("monday")
tue = Node("tuesday")
wed = Node("wednesday")
thu = Node("thursday")
fri = Node("friday")
sat = Node("saturday")
sun = Node("sunday")

mon.next = tue
tue.next = wed
wed.next = thu
thu.next = fri
fri.next = sat
sat.next = sun
sun.next = mon

print(mon.has_cycle())
