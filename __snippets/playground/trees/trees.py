from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self._age = 666

    __lst = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value



    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        if self.value < value:
            if self.right is None:
                self.right = Node(value)
                return
            else:
                self.right.insert(value)

        if self.value > value:
            if self.left is None:
                self.left = Node(value)
                return
            else:
                self.left.insert(value)

    def print(self):
        self.__lst = []
        if self.left:
            self.left.print()
        print(self.value)
        if self.right:
            self.right.print()

    def flatten(self):
        self.__lst = []
        if self.left:
            self.left.flatten()
        self.__lst.append(self.value)
        if self.right:
            self.right.flatten()
        return self.__lst

    def get_lst(self):
        print(self.__lst)
        print(Node.__lst)


node = Node(1)
node.insert(6)
node.insert(7)
node.insert(-1)

# print(node.age)
node.age = 55
print(node.age)

def test_tree():
    node = Node(randint(1, 1000000))
    for i in range(randint(1, 1000)):
        node.insert(randint(1, 1000000))
    tree_list = node.flatten()
    print(f"len: {len(tree_list)}")
    assert tree_list == sorted(tree_list)
    print("success...")

for i in range(5000):
    test_tree()