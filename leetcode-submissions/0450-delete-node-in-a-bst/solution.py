# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #using predecessor, largest value smaller than the key root
    def predecessor(self, root):
        curr = root.left
        while curr is not None and curr.right is not None:
            curr = curr.right
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None and root.right is not None:
                return root.right
            if root.right is None and root.left is not None:
                return root.left
            else:
                succ = self.predecessor(root)
                root.val = succ.val
                root.left = self.deleteNode(root.left, succ.val)
        return root
