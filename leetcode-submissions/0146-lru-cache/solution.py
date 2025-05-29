class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key : node

        # Left = LRU and Right = MRU
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next, self.right.prev = (
            self.right,
            self.left,
        )  # They point at each other initally

    def remove_from_list(self, node: Optional[ListNode]) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert_in_list(self, node: Optional[ListNode]) -> None:
        right = self.right
        mru = self.right.prev
        mru.next, node.prev = node, mru
        node.next, self.right.prev = right, node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_in_list(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            node.val = value
            self.insert_in_list(node)
            self.cache[key] = node

        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.insert_in_list(new_node)

            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove_from_list(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

