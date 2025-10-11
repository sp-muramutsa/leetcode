class TrieNode:
    def __init__(self):
        self.children = [None] * 26
    
    def contains(self, key: chr) -> bool:
        return self.children[ord("a") - ord(key)] is not None

    def put(self, key: chr, node: "TrieNode") -> None:
        self.children[ord("a") - ord(key)] = node

    def get(self, key: chr) -> "TrieNode":
        return self.children[ord("a") - ord(key)]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, prefix):

        curr = self.root
        n = len(prefix)
        i = 0
        flag = True

        for char in word:
    
            if i < n:
                if char != prefix[i]:
                    flag = False
                else:
                    i += 1

            if not curr.contains(char):
                curr.put(char, TrieNode())
            curr = curr.get(char)

        return flag and i == n
    
    # def startswith(self, word, prefix):

    #     curr = self.root

    #     for char in word:
    #         if not curr.contains(char):
    #             return False
    #         curr = curr.get(char)
        
    #     return True


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        trie = Trie()
        count = 0
        for word in words:
            if trie.insert(word, pref):
                count += 1
        
        return count

        
        
