# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        stack = []
        curr = root
        traversal = []

        while stack or curr:  
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            traversal.append(curr.val)
            curr = curr.right
        
        return traversal

