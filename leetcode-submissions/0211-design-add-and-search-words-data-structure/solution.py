class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def set_child(self, key: chr, node: "TrieNode") -> None:
        self.children[ord(key) - ord("a")] = node

    def get_child(self, key: chr) -> "TrieNode":
        return self.children[ord(key) - ord("a")]

    def contains_child(self, key: chr) -> bool:
        return self.children[ord(key) - ord("a")] is not None

    def set_end(self) -> None:
        self.is_end = True

    def check_end(self) -> bool:
        return self.is_end


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.contains_child(char):
                node = TrieNode()
                curr.set_child(char, node)
            curr = curr.get_child(char)
        curr.set_end()

    def search(self, word: str) -> bool:

        n = len(word)

        def dfs(node, idx):
            if not node:
                return False

            if idx == n:
                return node.check_end()

            if word[idx] == ".":
                for child in node.children:
                    if child and dfs(child, idx + 1):
                        return True
                return False
            else:
                if node.contains_child(word[idx]):
                    child = node.get_child(word[idx])
                    return dfs(child, idx + 1)
                else:
                    return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

