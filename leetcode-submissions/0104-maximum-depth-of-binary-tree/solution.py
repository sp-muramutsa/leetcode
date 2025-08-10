# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case if root is None return 0
        if root is None:
            return 0
        # Using BFS 
        length = 0
        # Identify the BFS function
        def BFS(root):
            # Identify your queue
            queue = deque()
            queue.append(root)
            # Identify your length
            length = 0
            # While the queue is not empty
            while queue:
                l = len(queue)
                # Update the length
                length += 1
                # Pop from the queue and add the children if available
                for i in range(l):
                    node = queue.popleft()
                    if node.right is not None:
                        queue.append(node.right)
                    if node.left is not None:
                        queue.append(node.left)
            # Return the length
            return length
        return BFS(root)
