# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder = [3,9,20,15,7],
        inorder = [9,3,15,20,7]

        - root = 3
        - find idx of root in inorder: 3
            - root.left = 0 to idx  [9]
            - root.right = idx + 1, to n [15, 20, 7]

        - For 9: 0 to parent_idx
        - len() == 4: return a new node

        - low = 0, up = 5, i = 0
        - if low == up:
            - return None
        - find idx in inorder
            - idx = 1
            root = TreeNode(preorder[i])
            - root.left = f(0, idx, i + 1)
            - root.right = f(idx + 1, n, i + 1)
        """
        n = len(preorder)
        self.i = 0

        def builder(low, high):

            if low == high:
                return

            if self.i == n:
                return

            idx = inorder.index(preorder[self.i])
            root = TreeNode(preorder[self.i])
            self.i += 1
            
            root.left = builder(low, idx)
            root.right = builder(idx + 1, high)

            return root

        return builder(0, n)

