# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative solution
# Time: Average is O(h) and worst case is O(n) in case of a linked list
# Space: Worst is O(n) in case of linked list
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = []
        traversal = []
        current = root # Pointer to the current node

        while current or stack:
            # Traverse the left part of the tree while stacking the nodes
            while current:
                stack.append(current)
                current = current.left
            
            # Pop from the stack and traverse the right side of the tree.
            # The pointer goes to the node that we just popped
            current = stack.pop()
            traversal.append(current.val)
            current = current.right
        
        return traversal

            





    
