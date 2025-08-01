class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def contains_child(self, key: chr) -> bool:
        return self.children[ord(key) - ord("a")] is not None

    def set_child(self, key: chr, node: "TrieNode") -> None:
        self.children[ord(key) - ord("a")] = node

    def get_child(self, key: chr) -> "TrieNode":
        return self.children[ord(key) - ord("a")]

    def children_count(self) -> int:
        return 26 - self.children.count(None)

    def return_first_child_char(self) -> str:
        for i in range(26):
            if self.children[i] is not None:
                return chr(i + ord("a"))

    def set_end(self) -> None:
        self.is_end = True

    def check_end(self) -> bool:
        return self.is_end


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word) -> None:
        curr = self.root
        for char in word:
            if not curr.contains_child(char):
                node = TrieNode()
                curr.set_child(char, node)
            curr = curr.get_child(char)
        curr.set_end()

    def get_lcp(self) -> str:

        path = []

        def dfs(node):
            if not node:
                return

            if node.children_count() == 1:
                char = node.return_first_child_char()
                path.append(char)
                child = node.get_child(char)

                if child.check_end():
                    return
                else:
                    return dfs(child)

        dfs(self.root)
        return "".join(path)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            if not word:
                return ""
            trie.addWord(word)

        return trie.get_lcp()

