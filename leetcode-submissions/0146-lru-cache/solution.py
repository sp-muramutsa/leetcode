class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        # Left = LRU, Right= MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove_from_list(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert_in_list(self, node):

        prev = self.right.prev

        self.right.prev = node
        node.next = self.right
        node.prev = prev
        prev.next = node

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]

            # Delete the node from the linked list
            self.remove_from_list(node)

            # Re insert it as the MRU
            self.insert_in_list(node)

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # Delete the node from the linked list
            self.remove_from_list(node)

            # Re insert it as the MRU
            self.insert_in_list(node)

        else:
            node = Node(key, value)

            # Insert it in hashmap
            self.cache[key] = node

            # Insert the it in linked list
            self.insert_in_list(node)

            # Check for overflow
            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove_from_list(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

