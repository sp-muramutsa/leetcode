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
            
        q = deque([root])
        traversal = []

        while q:

            level = []
            temp = []

            for x in q:
                temp.append(x.val)
                if x.left:
                    level.append(x.left)
                if x.right:
                    level.append(x.right)
            
            q = level
            traversal.append(temp)
        
        return traversal
        
