# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Top to bottom
        # At each node, the sum can:
            # be node + node.left
            # or node + node.right
        # We check the final sum when we get to the leaves

        if not root:
            return False
        
        self.exists = False
        def dfs(node, total):

            if not node:
                return

            if not node.left and not node.right:
                if node.val + total == targetSum:
                    self.exists = True 
                return
            
            # Recursively visit the node's children
            total += node.val
            dfs(node.left, total)
            dfs(node.right, total)

            # Backtrack and remove this node   
            total -= node.val
        
        dfs(root, 0)
        return self.exists

