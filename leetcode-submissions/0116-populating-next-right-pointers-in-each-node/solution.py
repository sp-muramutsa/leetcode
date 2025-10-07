"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        
        if not root:
            return root
        
        q = []
        if root.left:
            q.append(root.left)
        
        if root.right:
            q.append(root.right)

        while q:

            new_q = []
            n = len(q)

            for i in range(n - 1):
                q[i].next = q[i + 1]

                if q[i].left:
                    new_q.append(q[i].left)

                if q[i].right:
                    new_q.append(q[i].right)

                if q[i + 1].left:
                    new_q.append(q[i + 1].left)

                if q[i + 1].right:
                    new_q.append(q[i + 1].right)

            q = new_q

        return root

