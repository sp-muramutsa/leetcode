# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Using BFS to solve this problem
        # Edge case: the root node might be empty, we return []
        if root is None:
            return []
        # Define our result list that stores lists of values at each level of the tree
        result = []
        # Define a queue to store nodes
        queue = deque()
        # Add the root node
        queue.append(root)
        # While queue 
        while queue:
            # get the length of the queue
            length = len(queue)
            # Define the array for the level
            arr = []
            # Iterate the length of level
            for i in range(length):
                node = queue.popleft()
                # Pop the queue and add the val and add the left and then right if available
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(arr)
        return result
