class MyHashSet:

    def __init__(self):
        self.key_set = set()
        

    def add(self, key: int) -> None:
        self.key_set.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.key_set:
            self.key_set.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.key_set
 
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
