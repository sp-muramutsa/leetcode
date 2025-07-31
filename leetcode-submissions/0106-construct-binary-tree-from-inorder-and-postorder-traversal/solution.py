# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        n = len(postorder)
        self.i = n - 1
        inorder_indices = {val: idx for idx, val in enumerate(inorder)}

        def builder(low, high):

            if self.i < 0:
                return

            if low == high:
                return

            idx = inorder_indices[postorder[self.i]]
            root = TreeNode(postorder[self.i])
            self.i -= 1

            root.right = builder(idx + 1, high)
            root.left = builder(low, idx)

            return root

        return builder(0, n)

