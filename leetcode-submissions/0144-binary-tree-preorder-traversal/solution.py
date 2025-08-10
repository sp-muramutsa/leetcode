# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Define the helper function
        # While stack or curr
        # Pop from the stack and dd the node's value to the result list
        # if node.right is not none add it to the stack
        # if noe.left is not none add it to the stack
        result = []
        def iterative(root):
            curr = root
            stack = []
            while curr or stack:
                while curr:
                    result.append(curr.val)
                    stack.append(curr.right)
                    curr = curr.left
                curr = stack.pop()
        iterative(root)
        return result
