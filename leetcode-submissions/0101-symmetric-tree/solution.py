# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        self.mirror = True

        def dfs(node1, node2):

            if not node1 and not node2:
                return

            if not node1 or not node2:
                self.mirror = False
                return

            if node1.val != node2.val:
                self.mirror = False
                return

            dfs(node1.left, node2.right)
            dfs(node1.right, node2.left)

        dfs(root.right, root.left)
        return self.mirror

