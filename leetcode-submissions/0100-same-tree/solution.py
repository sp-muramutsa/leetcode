# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        same = True

        def dfs(x, y):
            
            nonlocal same
            if not x and not y:
                return 

            if not x or not y:
                same = False
                return
            
            if x.val != y.val:
                same = False
                return
            
            dfs(x.left, y.left)
            dfs(x.right, y.right)
        
        dfs(p, q)
        return same
