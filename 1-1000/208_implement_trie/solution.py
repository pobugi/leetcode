class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def __str__(self):
        return f"{self.children}"

    def __repr__(self):
        return f"{self.children}"


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("aeroplane")
param_2 = obj.search("aeroplane")
param_21 = obj.search("aeropfane")
param_3 = obj.startsWith("aero")

assert True