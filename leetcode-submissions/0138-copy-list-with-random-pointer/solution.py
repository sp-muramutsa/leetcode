"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        new = Node(0)
        count = 0
        while curr:
            copy = hashmap[curr]
            if count == 0:
                new.next = copy
            copy.next = (hashmap[curr.next])
            copy.random = (hashmap[curr.random])
            count += 1
            curr = curr.next
        return new.next

