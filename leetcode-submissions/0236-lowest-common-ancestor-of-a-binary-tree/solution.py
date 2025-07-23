# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Traverse with dfs till we reach p. keep its ancestors
        # Traverse with dfs till we reach q. keep its ancestors
        # Find the LCA in the ancestors list

        def get_ancestors(root, target, path):
            
            # Terminal
            if not root:
                return False
            
            # Goal
            path.append(root)
            if root == target:
                return True
            
            # Recursive
            if get_ancestors(root.left, target, path):
                return True
        
            
            if get_ancestors(root.right, target, path):
                return True
            
            path.pop()     
            
        
        p_ancestors = []
        get_ancestors(root, p, p_ancestors)
        
        q_ancestors = []
        get_ancestors(root, q, q_ancestors)

      
        seen = set(q_ancestors)
        i = len(p_ancestors) - 1
        
        while i >= 0:
            if p_ancestors[i] in seen:
                return p_ancestors[i]
            i -= 1
           
