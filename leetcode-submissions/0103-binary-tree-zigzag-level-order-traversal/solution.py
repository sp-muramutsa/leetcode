# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = [root]
        reverse = False
        zigzag = []

        while q:

            level = []
            temp = []

            for x in q:
                temp.append(x.val)
                if x.left:
                    level.append(x.left)
                if x.right:
                    level.append(x.right)

            if reverse:
                temp.reverse()

            zigzag.append(temp)
            q = level
            reverse = not reverse
        
        return zigzag


