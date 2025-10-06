# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        total = 0

        def f(node, curr_sum):

            if not node:
                return
                
            if not node.right and not node.left:
                nonlocal total
                curr_sum = (curr_sum * 10) + node.val
                total += curr_sum
                return 

            curr_sum = (curr_sum * 10) + node.val
            f(node.left, curr_sum)
            f(node.right, curr_sum)
            curr_sum /= 10
        
        f(root, 0)
        return total 
