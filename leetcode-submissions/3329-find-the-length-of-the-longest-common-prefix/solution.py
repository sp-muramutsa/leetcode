class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.is_end = False

    def contains_digit(self, key: str) -> bool:
        return self.children[ord(key) - ord("0")] is not None

    def set_digit(self, key: str, node: "TrieNode") -> None:
        self.children[ord(key) - ord("0")] = node

    def get_digit(self, key: str) -> None:
        return self.children[ord(key) - ord("0")]

    def set_end(self) -> None:
        self.is_end = True

    def check_end(self) -> bool:
        return self.is_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_number(self, number: int) -> None:
        curr = self.root
        number = str(number)

        for digit in number:
            if not curr.contains_digit(digit):
                node = TrieNode()
                curr.set_digit(digit, node)
            curr = curr.get_digit(digit)
        curr.set_end()

    def longest_prefix(self, number: int) -> int:

        number = str(number)
        n = len(number)
        length = 0

        def dfs(node, idx):
            if not node:
                return

            if idx == n:
                return

            if node.contains_digit(number[idx]):
                nonlocal length
                length += 1
                child = node.get_digit(number[idx])
                return dfs(child, idx + 1)

        dfs(self.root, 0)
        return length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        trie = Trie()
        for num1 in arr1:
            trie.insert_number(num1)

        longest_prefix = 0

        for num2 in arr2:
            num_common_prefix = trie.longest_prefix(num2)
            longest_prefix = max(longest_prefix, num_common_prefix)

        return longest_prefix

