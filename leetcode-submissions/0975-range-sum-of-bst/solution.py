# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        self.range_sum = 0

        def dfs(node):
            if not node:
                return

            if low <= node.val <= high:
                self.range_sum += node.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return self.range_sum
