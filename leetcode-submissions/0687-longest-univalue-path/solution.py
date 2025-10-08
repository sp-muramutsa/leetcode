# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        max_len = 0

        def dfs(node, prev):

            if not node:
                return 0
            
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            nonlocal max_len
            max_len = max(max_len, left + right)

            if node.val == prev:
                return 1 + max(left, right)
            else:
                return 0
            
        
        dfs(root, -1001)
        return max_len
