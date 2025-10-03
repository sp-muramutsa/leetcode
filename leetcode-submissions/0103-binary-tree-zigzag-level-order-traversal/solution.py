# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        position = 0
        
        while queue:
            nodes_in_current_level = len(queue)
            holder = []
            
            for node in queue:
                holder.append(node.val)
            
            if position == 0:
                ans.append(holder)
                position = 1
            else:
                ans.append(holder[::-1])
                position = 0
                
            
            for i in range(nodes_in_current_level):
                current_node = queue.popleft()
                
                if current_node.left:
                    queue.append(current_node.left)
                    
                if current_node.right:
                    queue.append(current_node.right)
                    
        return ans
        
