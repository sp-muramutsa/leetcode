# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS Solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        q = [root] if root is not None else None
        height = 0

        while q:
            height += 1
            children = []
            for node in q:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            q = children

        return height

