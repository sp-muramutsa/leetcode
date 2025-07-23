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

        dq = deque([root])

        traversal = []
        left_to_right = True

        while dq:     
            level = []
            k = len(dq)

            for _ in range(k):
                
                if left_to_right:
                    node = dq.pop()     
                    level.append(node.val)

                    if node.left:
                        dq.appendleft(node.left)
                    
                    if node.right:
                        dq.appendleft(node.right)
                
                else:
                    node = dq.popleft()          
                    level.append(node.val)

                    if node.right:
                        dq.append(node.right)
                    
                    if node.left:
                        dq.append(node.left)
            
            left_to_right = not left_to_right
            traversal.append(level)
        
        return traversal
            


