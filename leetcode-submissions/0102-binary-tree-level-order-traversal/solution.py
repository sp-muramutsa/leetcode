# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        traversal = []
        q = [root]

        while q:
            temp = []
            for node in q:
                temp.append(node.val)
            traversal.append(temp)

            children = []
            for node in q:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            q = children

        return traversal

