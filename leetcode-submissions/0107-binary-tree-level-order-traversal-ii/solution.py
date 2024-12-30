# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same solution for I but insert at the start
from collections import deque


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        if not root:
            return traversal
        q = deque([root])

        while q:
            level = len(q)
            level_traversal = []

            for _ in range(level):
                current = q.popleft()
                level_traversal.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            traversal.insert(0, level_traversal)

        return traversal

