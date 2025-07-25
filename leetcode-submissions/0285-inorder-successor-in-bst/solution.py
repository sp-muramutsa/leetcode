# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        """
        In a BST, an inorder successor is the node with the smallest key greater than p.val

        Intuition:
        - We can traverse the tree downwards
        - Anytime we see a larger value than p, we update the result and move left
        - Otherwise, we move right.
        """
       
        curr = root
        res = None
        
        while curr:  
            if curr.val > p.val:
                res = curr
                curr = curr.left   
            else:
                curr = curr.right
        
        return res

        

