class TrieNode:
    def __init__(self):
        self.alphabets = [None] * 26
        self.is_end = False

    def contains_key(self, key: str) -> bool:
        return self.alphabets[ord(key) - ord("a")] is not None

    def get(self, key: str) -> "TrieNode":
        return self.alphabets[ord(key) - ord("a")]

    def put(self, key: str, node: "TrieNode"):
        self.alphabets[ord(key) - ord("a")] = node

    def set_end(self) -> None:
        self.is_end = True

    def check_end(self) -> bool:
        return self.is_end


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if not curr.contains_key(char):
                curr.put(char, TrieNode())
            curr = curr.get(char)
        curr.set_end()

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if curr.contains_key(char):
                curr = curr.get(char)
            else:
                return False

        if curr.check_end():
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if curr.contains_key(char):
                curr = curr.get(char)
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

