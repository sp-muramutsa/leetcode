# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        res = 0

        while stack:
            n, l = stack.pop()
            res = max(res, l)
            if n.right:
                stack.append((n.right, l+1))

            if n.left:
                stack.append((n.left, l+1))

        return res
