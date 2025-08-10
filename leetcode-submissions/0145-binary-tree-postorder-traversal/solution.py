# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Using recursion
        # Define your helper function
        # Define your result list
        # if root is None return 
        # Recursively call the function on the left child
        # Recursively call the function on the right child
        result = []
        def recursion(root):
            if root is None:
                return
            
            recursion(root.left)
            recursion(root.right)
            result.append(root.val)
        recursion(root)
        return result
