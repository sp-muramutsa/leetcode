# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - preorder = [3,9,20,15,7]
        - inorder = [9,3,15,20,7]

        - start with 3 (first in preorder)
        - find the index of 3 in the inorder array
        - i = 0
        - l, r = 0, 4
        - [3].left = [9]
        - [3].right = [15, 20, 7]

        - i = 1
        - l, r = 0, 1
        - [9]

        - i = 3
        - [20]
        - l, r = 1, 4
        """

        inorder_indices = {x: i for i, x in enumerate(inorder)}
        n = len(preorder)
        i = 0

        def f(left, right):

            nonlocal i
            if i >= n:
                return None

            if left == right:
                return None

            inorder_idx = inorder_indices[preorder[i]]
            node = TreeNode(inorder[inorder_idx])
            i += 1
            node.left = f(left, inorder_idx)
            node.right = f(inorder_idx + 1, right)
            return node

        return f(0, n)

