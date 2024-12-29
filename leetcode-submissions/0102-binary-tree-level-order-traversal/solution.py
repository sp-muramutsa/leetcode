# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative using deque from collections
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        if not root:
            return traversal

        queue = deque([root])

        while queue:
            # Get level
            level = len(queue)
            level_traversal = []

            # Iterate  throught the queue while popping nodes on the current level.
            # i.e. Pop the leftmost node(FIFO) and add it to the list of the current traversal
            # Add children to the queue: Left child, then right child.
            for _ in range(level):
                current = queue.popleft()
                level_traversal.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            traversal.append(level_traversal)

        return traversal

