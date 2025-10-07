# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if not root:
            return 0
        
        graph = defaultdict(list)


        

        queue = deque([root])
        while queue:
            current_node = queue.popleft()
            
            if current_node.left:
                graph[current_node.val].append(current_node.left.val)
                graph[current_node.left.val].append(current_node.val)

                queue.append(current_node.left)

            if current_node.right:
                graph[current_node.val].append(current_node.right.val)
                graph[current_node.right.val].append(current_node.val)

                queue.append(current_node.right)

        seen = set()
        def bfs(node, level):
            queue = deque([node])
            distance = 0
            while queue and (distance < level):
                step = len(queue)

                for i in range(step):
                    current_node = queue.popleft()
                    seen.add(current_node)
                    for neighbour in graph[current_node]:
                        if neighbour not in seen:
                            queue.append(neighbour)
                

                distance += 1

            return list(queue)
        
        return bfs(target.val,k)
