# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [root]
        depth = 0
        curr = root

        while stack:

            level = []
            for node in stack:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            stack = level
            depth += 1

        return depth

