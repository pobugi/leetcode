from random import randint


class Node:
    def __init__(self, value, level=None):
        self.left = None
        self.right = None
        self.value = value
        self.level = level

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"value: {self.value}; left: {self.left}, right: {self.right}"

    def insert(self, value):
        if not self.value:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = Node(value=value, level=self.level + 1)
            else:
                self.left.insert(value=value)
        if value > self.value:
            if self.right is None:
                self.right = Node(value=value, level=self.level + 1)
            else:
                self.right.insert(value=value)

    def print(self):
        print(f"called print func for the node: {self.value}")
        if self.left:
            self.left.print()
        # print(f"value: {self.value}; level: {self.level}", end="\n")
        if self.right:
            self.right.print()


root = Node(value=5, level=0)

for i in [1,2,4,5,6,7,8,10]:
    root.insert(i)

root.print()
