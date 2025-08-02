class TrieNode:
    def __init__(self, value: str):
        self.children = [None] * 26
        self.is_end = False
        self.value = value

    def contains_child(self, key: chr) -> bool:
        return self.children[ord(key) - ord("a")] is not None

    def get_child(self, key: chr) -> "TrieNode":
        return self.children[ord(key) - ord("a")]

    def set_child(self, key: chr, node: "TrieNode") -> None:
        self.children[ord(key) - ord("a")] = node

    def set_end(self) -> None:
        self.is_end = True

    def check_end(self) -> bool:
        return self.is_end


class Dictionary:
    def __init__(self):
        self.root = TrieNode("$ROOT")

    def insert(self, word: str) -> None:

        curr = self.root

        for char in word:
            if not curr.contains_child(char):
                node = TrieNode(char)
                curr.set_child(char, node)
            curr = curr.get_child(char)

        curr.set_end()


class Solution:
    def backtracking_search(
        self,
        cell: tuple,
        board: List[List[str]],
        dictionary: Dictionary,
        m: int,
        n: int,
    ) -> List[str]:

        result = set()

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(row, col, node, visited, path):

            if board[row][col] == "#":
                return

            # If the trie doesn't contain this char, return
            if not node.contains_child(board[row][col]):
                return

            path.append(board[row][col])
            node = node.get_child(board[row][col])
            char = board[row][col]
            board[row][col] = "#"

            # If there is a word that ends here, put it in the result
            if node.check_end():
                word = "".join(path)
                result.add(word)

            for dx, dy in movements:
                x, y = row + dx, col + dy
                if 0 <= x < m and 0 <= y < n:
                    backtrack(x, y, node, visited, path)

            # visited.remove((row, col))
            path.pop()
            board[row][col] = char

        r, c = cell
        backtrack(r, c, dictionary.root, set(), [])
        return result

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])
        found = set()
        dictionary = Dictionary()

        for word in words:
            dictionary.insert(word)

        for r in range(m):
            for c in range(n):
                existing_words = self.backtracking_search(
                    (r, c), board, dictionary, m, n
                )
                found = found.union(existing_words)

        return list(found)

