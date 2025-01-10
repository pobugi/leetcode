class RandomizedSet:

    def __init__(self):
        self.items = set()
        self.hash_set = dict() # {value: {deleted: False}}

    def insert(self, val: int) -> bool:
        if val in self.hash_set and self.hash_set[val]["deleted"] is False:
            return False
        self.hash_set[val] = {"deleted": False}
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash_set and self.hash_set[val]["deleted"] is False:
            self.hash_set[val] = {"deleted": True}
            return True
        return False

    def getRandom(self) -> int:
        while True:
            index = randint(0, len(self.hash_set) - 1)
            key = list(self.hash_set.keys())[index]
            if self.hash_set[key]["deleted"] is False:
                return key



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()