class TrieNode:
    def __init__(self) -> "TrieNode":
        self.children = [None] * 26
        self.is_end = False

    def contains(self, key: chr) -> bool:
        return self.children[ord("a") - ord(key)] is not None

    def put(self, key: chr, node: "TrieNode") -> None:
        self.children[ord("a") - ord(key)] = node

    def get(self, key: chr) -> "TrieNode":
        return self.children[ord("a") - ord(key)]

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
            if not curr.contains(char):
                node = TrieNode()
                curr.put(char, node)
            curr = curr.get(char)
        
        curr.set_end()
        

    def search(self, word: str) -> bool:
        
        curr = self.root 

        for char in word:
            if not curr.contains(char):
                return False
            curr = curr.get(char)
        
        return curr.check_end()

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for char in prefix:
            if not curr.contains(char):
                return False
            curr = curr.get(char)
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
