# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float("-inf")

        def f(node):

            if not node:
                return 0
            
            l = f(node.left)
            r = f(node.right)

            l = max(l, 0)
            r = max(r, 0)

            nonlocal ans  
            ans = max(ans, l + node.val + r)   
            return node.val + max(l, r)
        
        f(root)
        return ans
