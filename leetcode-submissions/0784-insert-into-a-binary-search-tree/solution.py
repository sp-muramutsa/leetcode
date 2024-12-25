# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #we create a treenode instance with our key given
        temp = TreeNode(val)

        if root is None:
            return TreeNode(val)

        parent = None
        curr = root
        while curr is not None:
            parent = curr
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
            else:
                return root
        if parent.val > val:
            parent.left = temp
        elif parent.val < val:
            parent.right = temp
        else:
            return root
        return root
