class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end = False

    def set_child(self, key: chr, node: "TrieNode") -> None:
        self.children[ord(key) - ord("a")] = node

    def get_child(self, key: chr) -> "TrieNode":
        return self.children[ord(key) - ord("a")]

    def contains_child(self, key: chr) -> bool:
        return self.children[ord(key) - ord("a")] is not None

    def check_end(self) -> bool:
        return self.is_end

    def set_end(self) -> bool:
        self.is_end = True


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.contains_child(char):
                node = TrieNode()
                curr.set_child(char, node)
            curr = curr.get_child(char)
        curr.set_end()

    def search(self, word: str) -> bool:

        curr = self.root
        for char in word:
            if not curr.contains_child(char):
                return False
            curr = curr.get_child(char)

        return curr.check_end()

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.contains_child(char):
                return False
            curr = curr.get_child(char)

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

