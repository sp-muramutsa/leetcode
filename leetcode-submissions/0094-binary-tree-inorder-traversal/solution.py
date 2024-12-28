# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #so we need a node that points to the node we are at, and it starts at root.
        node = root
        #we use a stacl to store the nodes we have visited the same way the recursion works.
        stack = []
        #the list for the nodes values.
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            #this means we are at the leaf or node without left
            #we set the node pointer to the previous node as it is Null at the moment
            node = stack.pop()
            #we add the value to the result
            result.append(node.val)
            node = node.right
        return result

