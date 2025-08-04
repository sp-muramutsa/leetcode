# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        self.i = 0
        inorder = sorted(preorder)
        inorder_indices = {val: idx for idx, val in enumerate(inorder)}

        def builder(low, high):

            if low == high:
                return

            if self.i == n:
                return

            idx = inorder_indices[preorder[self.i]]
            root = TreeNode(preorder[self.i])
            self.i += 1
            
            root.left = builder(low, idx)
            root.right = builder(idx + 1, high)

            return root

        return builder(0, n)
