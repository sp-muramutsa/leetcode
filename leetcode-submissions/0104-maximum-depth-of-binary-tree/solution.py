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
        q = [root]
        max_len = 0

        while q:

            new_q = []
            for x in q:
                if x.left:
                    new_q.append(x.left)
                if x.right:
                    new_q.append(x.right)
            
            q = new_q
            
            max_len += 1
        
        return max_len

