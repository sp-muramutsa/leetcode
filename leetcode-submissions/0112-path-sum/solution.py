# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        flag = False
        def dfs(node, total):
            
            if not node:
                return

            if not node.right and not node.left:
                nonlocal flag
                if total + node.val == targetSum:
                    flag = True
                return

            total += node.val
            dfs(node.left, total)
            dfs(node.right, total)
            total -= node.val

        dfs(root, 0)
        return flag

