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

        stack = deque([root])

        while stack:
            k = len(stack)
            for _ in range(k):
                node = stack.pop()

                if node.left:
                    stack.appendleft(node.left)

                if node.right:
                    stack.appendleft(node.right)

            l = len(stack)
            for i in range(l - 1, 0, -1):
                stack[i].next = stack[i - 1]

        return root
