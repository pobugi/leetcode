from typing import Optional


class Node:
    def __init__(self, value: int | None = None):
        self.value = value
        self.next: Optional["Node"] = None
        # self.__create_list()

    def __repr__(self):
        return f"Node: {self.value}"


class LinkedList:
    def __init__(self, root: Node | None = None):
        self.root = root
        self.tail = root
        self.length: int = 1

    def __repr__(self):
        return f"Root: {self.root}; tail: {self.tail}, length: {self.length}"

    def get(self, index: int) -> int:
        # int get(int index)
        # Get the value of the indexth node in the linked list.
        # If the index is invalid, return -1.
        node = self.getNode(index)
        return node.value if node else -1

    def getNode(self, index) -> Node | None:
        if index > self.length - 1 or index < 0:
            return None
        curr = self.root
        for i in range(index):
            curr = curr.next
        return curr

    def addAtHead(self, val: int) -> None:
        # void addAtHead(int val)
        # Add a node of value val before the first element of the linked list.
        # After the insertion, the new node will be the first node of the linked list.
        node = Node(val)

        if not self.root:
            self.root = node
            self.tail = self.root
        else:
            root = self.root
            node.next = root
            self.root = node
            self.tail = root
        self.length += 1

    def addAtTail(self, val: int) -> None:
        # void addAtTail(int val)
        # Append a node of value val as the last element of the linked list.
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # void addAtIndex(int index, int val)
        # Add a node of value val before the indexth node in the linked list.
        # If index equals the length of the linked list, the node will be appended
        # to the end of the linked list.
        # If index is greater than the length, the node will not be inserted.
        if index == self.length:
            return self.addAtTail(val)
        if index < 0:
            return None
        if index == 0:
            return self.addAtHead(val)
        prev = self.getNode(index - 1)
        curr = prev.next

        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        # void deleteAtIndex(int index)
        # Delete the indexth node in the linked list, if the index is valid.
        if index < 0 or index > self.length:
            return None
        if index == 0:
            if self.length == 1:
                self.root, self.tail = None, None
                self.length = 0
            elif self.length == 2:
                x = self.root.next
                self.root, self.tail = x
                self.length = 1
            else:
                x = self.root.next
                self.root = x
                self.length -= 1
        else:
            prev = self.getNode(index - 1)
            if prev.next:
                x = prev.next.next
                prev.next = x
            else:
                last = self.getNode(index - 2)
                last.next = None
                self.tail = last
            self.length -= 1
