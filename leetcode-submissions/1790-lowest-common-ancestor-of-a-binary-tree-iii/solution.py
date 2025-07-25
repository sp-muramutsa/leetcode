"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def get_ancestors(node, ancestry):

            while node:
                ancestry.append(node)
                node = node.parent
            
            return ancestry
        
        p_fam = get_ancestors(p, [])
        q_fam = get_ancestors(q, [])
        
        seen = set(p_fam)

        for node in q_fam:
            if node in seen:
                return node
        
        


