from collections import deque
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if not edges:
            return True
        
        graph = defaultdict(list)
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
            
        visited = set()
            
        def bfs(node):
            ans = 0
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current_node = queue.popleft()
                
                for neighbour in graph[current_node]:
                    if neighbour == destination:
                        ans += 1
                    
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            return ans
                        
        ans = bfs(source)
        return ans > 0
