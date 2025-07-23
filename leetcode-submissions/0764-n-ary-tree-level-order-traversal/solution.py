"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:

        if not root:
            return []

        traversal = []
        q = deque([root])

        while q:

            k = len(q)
            level = []

            for _ in range(k):
                node = q.popleft()
                level.append(node.val)

                for child in node.children:
                    q.append(child)

            traversal.append(level)

        return traversal

