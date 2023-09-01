class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.root = None

    def push(self, value):
        node = Node(value=value)

    def print(self, node: Node):
        while node is not None:
            print(node.value)
            