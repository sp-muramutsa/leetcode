"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return

        # Create clones: A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr is not None:
            temp_next = curr.next
            clone = Node(curr.val)
            curr.next = clone
            clone.next = temp_next
            curr = temp_next

        # Update random in clone
        curr = head
        while curr is not None:
            clone = curr.next
            clone.random = curr.random.next if curr.random else None  # E
            curr = curr.next.next

        # Link clones and restore the original list
        curr = head
        clone_head = head.next
        curr_clone = clone_head

        while curr:
            curr.next = curr_clone.next
            curr_clone.next = curr_clone.next.next if curr_clone.next else None

            curr = curr.next
            curr_clone = curr_clone.next

        return clone_head

