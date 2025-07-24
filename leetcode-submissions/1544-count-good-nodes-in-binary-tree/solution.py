# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        def dfs(node, upper):

            if not node:
                return

            if node.val >= upper:
                nonlocal good_nodes
                good_nodes += 1
                upper = node.val

            dfs(node.left, upper)
            dfs(node.right, upper)

        upper_lim = float("-inf")
        dfs(root, upper_lim)
        return good_nodes

