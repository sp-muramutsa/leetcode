# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ROOT -> LEFT -> RIGHT
class Solution:
    def __init__(self):
        self.preorder = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.preorder.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.preorder
