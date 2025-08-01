class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_file = False
        self.contents = ""

    def contains_child(self, key: chr) -> bool:
        return key in self.children

    def set_child(self, key: chr, node: "TrieNode") -> "None":
        self.children[key] = node

    def get_child(self, key: chr) -> "TrieNode":
        if key in self.children:
            return self.children[key]

    def list_children(self) -> List:
        if self.is_file:
            return [self.name]
        else:
            children = [x.name for x in self.children.values()]
            return sorted(children)


class FileSystem:

    def __init__(self):
        self.root = TrieNode("root")

    def ls(self, path: str) -> List[str]:
        curr = self.root
        folders = path[1:].split("/")

        for char in folders:
            if not char:
                return curr.list_children()
            curr = curr.get_child(char)

        return curr.list_children()

    def traverse(self, path) -> "TrieNode":
        curr = self.root
        folders = path[1:].split("/")
        for char in folders:
            if not curr.contains_child(char):
                node = TrieNode(char)
                curr.set_child(char, node)
            curr = curr.get_child(char)
        return curr

    def mkdir(self, path: str) -> None:
        self.traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.traverse(filePath)
        curr.contents += content
        curr.is_file = True

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.traverse(filePath)
        return curr.contents


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

