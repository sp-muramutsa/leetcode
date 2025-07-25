# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_inorder_successor(self, node):
        """
        Smallest value on the right
        """
        curr = node.right

        while curr.left:
            curr = curr.left
        return curr

    def get_inorder_predecessor(self, node):
        """
        Largest element on the left
        """
        curr = node.left

        while curr.right:
            curr = curr.right
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Case 1: target not found
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:

            # Case 1: Target node is a leaf node: Simply prune it
            if not root.left and not root.right:
                return None

            # Case 2: Target node has only one child node: Replace it with its child
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # Case 3: Target node has two children nodes:
            # Replace target node with inorder successor or predecessor
            else:
                inorder_predecessor = self.get_inorder_predecessor(root)
                root.val = inorder_predecessor.val
                root.left = self.deleteNode(root.left, inorder_predecessor.val)

        return root

