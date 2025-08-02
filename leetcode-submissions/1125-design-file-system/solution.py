class TrieNode:
    def __init__(self):
        self.children = {}
        self.contents = ""

    def contains_folder(self, key: chr) -> bool:
        return key in self.children

    def set_folder(self, key: chr, node: "TrieNode") -> None:
        self.children[key] = node

    def get_folder(self, key: chr) -> "TrieNode":
        return self.children.get(key, None)


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:

        curr = self.root
        folders = path[1:].split("/")
        last = folders[-1]

        for char in folders[:-1]:
            if not curr.contains_folder(char):
                return False
            curr = curr.get_folder(char)

        # Last one
        if not curr.contains_folder(last):
            node = TrieNode()
            node.contents = value
            curr.set_folder(last, node)
            curr = curr.get_folder(last)
            return True
        else:
            return False

    def get(self, path: str) -> int:
        curr = self.root
        folders = path[1:].split("/")
        last = folders[-1]

        for char in folders[:-1]:
            if not curr or not curr.contains_folder(char):
                return -1
            curr = curr.get_folder(char)

        if curr and curr.contains_folder(last):
            last_node = curr.get_folder(last)
            return last_node.contents
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

