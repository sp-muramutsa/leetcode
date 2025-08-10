# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Identify the dfs function
        def dfs(root):
            # If we reached the end of the tree return
            if root is None:
                return
            # If the value of the root is greater than the target dfs the left
            if root.val > val:
                return dfs(root.left)
            # If the value of the root is less than the target dfs the right
            elif root.val < val:
                return dfs(root.right)
            # Else return root
            else:
                return root
        return dfs(root)
