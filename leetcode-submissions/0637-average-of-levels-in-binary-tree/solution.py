# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        averages = []
        q = deque([root])

        while q:

            level = []
            k = len(q)

            for _ in range(k):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            average = sum(level) / len(level)
            averages.append(average)
            
        
        return averages
        
